# Standard dev session

# Create new session, go to LLVM source dir.
new-session -d -s mips 'cd $HOME/work/llvm.git; exec $SHELL'

# Name window with LLVM code editor.
set-window-option -t 1 automatic-rename off
rename-window -t 1 'LLVM x86'

# Make new pane for building, debugging etc.
split-window -h -p 50 'cd $HOME/work/llvm.git; exec $SHELL'
select-pane -t 1.0

# Create new window for the Malta board connection.
new-window -t 2 'ssh malta'
set-window-option -t 2 automatic-rename off
rename-window -t 2 'LLVM MIPS'

# Select the first window and attach to created session.
select-window -t 1
