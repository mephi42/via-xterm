via-xterm: connect Python script to `xterm`
###########################################

Usage
=====

`via-xterm script [argument ...]`

Why?
====

To simplify debugging of scripts, that use escape sequences/ncurses/urwid, in
an IDE (e.g. PyCharm). Normally IDEs' integrated consoles do not handle all
escape sequences, so one has to either tolerate that or use remote debugging.
`via-xterm` allows to circumvent that by wrapping the target script in a way
that its stdin/stdout are connected to a new `xterm -S` instance, through
which a user can interact with it. Debugging target script is possible, because
it is run using `compile()` and `exec()` builtins.
