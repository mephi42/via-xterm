# Synopsis
Connect stdin/stdout of a Python script to `xterm`.

# Usage
`xterm-wrapper script [argument ...]`

# Why?
To simplify debugging of scripts, that use escape sequences/ncurses/urwid, in
an IDE (e.g. PyCharm). Normally IDEs' integrated consoles do not handle all
escape sequences, so one has either tolerate that or use remote debugging.
`via-xterm` allows to circumvent that by wrapping the desired script in a way
that its stdin/stdout are connected to an `xterm -S` instance.
