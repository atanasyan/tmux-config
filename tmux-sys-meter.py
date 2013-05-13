#!/usr/bin/python

import collections
import re
import subprocess
import time

def get_red(str):
  return "#[fg=colour9]%s#[fg=default]" % (str)

def get_yellow(str):
  return "#[fg=colour11]%s#[fg=default]" % (str)

def get_green(str):
  return "#[fg=colour10]%s#[fg=default]" % (str)

# return (total, used, free)
def get_memory_usage():
  mem_total       = 0
  mem_free        = 0
  mem_buffers     = 0
  mem_cached      = 0
  mem_swap_cached = 0

  p = re.compile('\d+')
  proc = open('/proc/meminfo','r')
  for line in iter(proc.readline,''):
    if line.startswith('MemTotal:'):
      mem_total = float(p.findall(line)[0])
    elif line.startswith('MemFree:'):
      mem_free = float(p.findall(line)[0])
    elif line.startswith('Buffers:'):
      mem_buffrs = float(p.findall(line)[0])
    elif line.startswith('Cached:'):
      mem_cached = float(p.findall(line)[0])
    elif line.startswith('SwapCached:'):
      mem_swap_cached = float(p.findall(line)[0])

  mem_free = mem_free + mem_buffers + mem_cached + mem_swap_cached
  mem_used = mem_total - mem_free
  return (mem_total, mem_used, mem_free)

# return (user, nice, system, idle)
def get_cpu_usage():
  p = re.compile('\d+')
  proc = open('/proc/stat','r')
  for line in iter(proc.readline,''):
    if line.startswith('cpu '):
      vals = p.findall(line)
      return (float(vals[0]), float(vals[1]), float(vals[2]), float(vals[3]))
  return ()

# get mem usage string
def get_mem_usage_str():
  stat = get_memory_usage()
  used = 0

  if stat:
    used = stat[1] / stat[0] * 100.0

  used_str = "Mem: %.0f%%" % (used)

  if used < 33:
    return get_green(used_str)
  elif used < 66:
    return get_yellow(used_str)
  else:
    return get_red(used_str)

# get cpu usage string
def get_cpu_usage_str(delay_sec):
  stat1 = get_cpu_usage()
  time.sleep((delay_sec * 1000000 - 100000) / 1000000.0)
  stat2 = get_cpu_usage()

  used = 0

  if stat1 and stat2:
    diff_user = stat2[0] - stat1[0]
    diff_nice = stat2[1] - stat1[1]
    diff_sys  = stat2[2] - stat1[2]
    diff_idle = stat2[3] - stat1[3]
    used = (diff_user + diff_nice + diff_sys) / \
           (diff_user + diff_nice + diff_sys + diff_idle) * 100.0

  used_str = "CPU: %.2f%%" % (used)

  if used < 33:
    return get_green(used_str)
  elif used < 66:
    return get_yellow(used_str)
  else:
    return get_red(used_str)

try:
  print "%s %s" % (get_cpu_usage_str(2), get_mem_usage_str())
except:
  print '[error]'
