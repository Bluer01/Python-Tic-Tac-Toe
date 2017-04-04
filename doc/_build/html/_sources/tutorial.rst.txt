Tutorial
*********************

How to start the game
=====================

.. note::
    You will need Python installed and it will need to be at least Python 3. Python 3 includes 
    changes that are not compatible with early versions, so to play this you will need at 
    least Python 3.

Just run **game.py** in your terminal/command line! Like so::

    cd \path\to\game
    python game.py

If you get an error that python isn't recognised as a command, it sounds like you don't have 
Python in your path, in which case I would advise you to do so. 

In Windows this can be done in the command line with::

    set PATH=%PATH%;\path\to\python

In Linux this can be done in the terminal with::

    export PATH=$PATH:/path/to/python

How to play
===========

I'm pretty sure most people have played Tic-Tac-Toe before, but I'll give you something to chew 
on anyway.

Setup & Objective
-----------------

So, you have a 3x3 grid, and you have a symbol that represents you on the board: an 'o' or an 'x'. 
Your objective is to line 3 of your symbol in a line, whether it be horizontal, vertical, or 
diagonal. Here are some examples of the 'x' winning::

    x | x | x          | x |            |   | x
   ---+---+---      ---+---+---      ---+---+---
      |   |            | x |            | x |   
   ---+---+---      ---+---+---      ---+---+---
      |   |            | x |          x |   |   

Flow of a round
---------------

When it's your turn, you will be asked to place your symbol somewhere on this grid. The grid space
must be empty, as in, no other symbol can be in that grid space. Once your symbol has been placed,
the next player takes their turn if you have not won with your decision.
