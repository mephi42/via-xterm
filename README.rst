.. image:: http://img.shields.io/pypi/v/via-xterm.svg
   :target: https://pypi.python.org/pypi/via-xterm

via-xterm: connect Python script to ``xterm``
#############################################

Usage
=====

``via-xterm script [argument ...]``

How is this useful?
===================

To simplify debugging of scripts, that use `escape sequences
<https://en.wikipedia.org/wiki/ANSI_escape_code>`_/`curses
<https://docs.python.org/3/howto/curses.html>`_/`urwid
<http://urwid.org/>`_, in an IDE (e.g. `PyCharm
<https://www.jetbrains.com/pycharm/>`_). Normally IDEs' integrated consoles do
not handle all the escape sequences, so one has to either live with that or
use remote debugging.

``via-xterm`` wraps the target script in a way that its stdin/stdout are
connected to a new `xterm -S
<https://linux.die.net/man/1/xterm>`_ instance, which handles the user
interaction. Debugging the target script is possible, because it is run using
``compile()`` and ``exec()`` builtins.
