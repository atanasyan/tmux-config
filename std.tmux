# Standard dev session

# Create new session, go to LLVM source dir.
new-session -d -s mips 'cd $HOME/work/llvm.git; exec $SHELL'

# Name window with LLVM code editor.
set-window-option -t 1 automatic-rename off
rename-window -t 1 'LLVM x86'

# Make a couple of panes for building, debugging etc.
split-window -h -p 50 -c $HOME/work/llvm.git
split-window -v -p 50 -c $HOME/work/sandbox

# Create window for the Malta board connection.
new-window -t 2 'ssh malta'
set-window-option -t 2 automatic-rename off
rename-window -t 2 'LLVM MIPS'

# Create window for MCLinker development
new-window -t 3 -c $HOME/work/mclinker.git
set-window-option -t 3 automatic-rename off
rename-window -t 3 'MCLinker'

# Make a couple of panes for building, debugging etc.
split-window -h -p 50 -c $HOME/work/mclinker.git
split-window -v -p 50 -c $HOME/work/mclinker/sandbox

# Select the zero pane in the first window
select-window -t 1
select-pane -t 1.0
