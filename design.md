My aim in this project: to develop a Conway's Game of Life implementation.


Notes
-----

  * 'Rewinding' is difficult: one possibility would be to intermittently record
    board positions so that to find a certain generation, you could revert to
    the floored closest board and add on as many more generations as needed.
    * Maybe for rewinding, make a HistoryCell class which stores its state
      history for given generations!


Classes
-------

### GameController

Controls a single game of Game of Life. A 'game' consists of a single Board
and a single RuleSet.

Jobs: tracks generation, allows stepping etc.


### Board

Tracks the state of a set of Cells.


### Cell

A cell with an arbitrary number of states.


Concepts
--------

### Board string

A board string defines a board's layout.

    25,10,10010010111010100101101001...

3 fields:

  * 1: number of columns (x)
  * 2: number of rows (y)
  * 3: cell string (state for each cell)

In class terms:

BoardStr = (x, y, GridStr)

Newlines and spaces are ignored, so feel free to format the string in whatever
visually pleasing way you would like.

If more than 3 fields are found (i.e. more than 2 commas), the string is
invalid.
