#!/usr/bin/env python3
#
# Generic 2D cellular automaton board.
#

from utils import *
from cell import Cell
from ruleset import RulesConway

class Board:
    """Generic cellular automaton board."""
    def __init__(self, ruleset, x_size, y_size, boardstr=""):
        """Initialise board."""
        self.ruleset = ruleset
        self.x = x_size
        self.y = y_size

        self.board = [Cell() for i in range(self.x * self.y)]
        if boardstr == "":
            # no state provided, initialise to all to state 0
            self.set_board(str(self.ruleset.get_base_state()) * self.x * self.y)
        else:
            self.set_board(boardstr)


    def next_gen(self):
        boardstr = ""
        for cell_index in range(len(self.board)):
            new_state = self.ruleset.get_cell_next(
                    self.board[cell_index],
                    self.get_neighbours(cell_index)
                    )
            boardstr += str(new_state)
        self.set_board(boardstr)

    def print_board(self):
        count = 0
        for cell in self.board:
            print(cell.get_state(), end="")
            count += 1
            if count == 5:
                count = 0
                print()

    def get_neighbours(self, cell):
        """Return all the neighbours of a cell index as an array of Cells."""
        neighbours = []

        cell_x = cell % self.x
        for cell_index in [
                cell-self.x-1, # UL
                cell-self.x,   # U
                cell-self.x+1, # UR
                cell+1,   # R
                cell+self.x+1, # DR
                cell+self.x,   # D
                cell+self.x-1, # DL
                cell-1    # L
                ]:
            if cell_index < 0:
                # NOTE: board *does not* wrap round, so no -ve indices allowed
                logging.debug("-ve neighbour cell: " + str(cell_index))
                continue
            if abs((cell_index % self.x) - cell_x) <= 1:
                # x difference is 1 or 0, so it's a neighbour
                # but, it might not exist (edge of board)
                try:
                    neighbours.append(self.board[cell_index])
                except IndexError:
                    logging.debug("not on board: " + str(cell_index))
                    continue

        return neighbours

    def set_board(self, boardstr):
        state = "".join(boardstr.split()) # remove all whitespace
        for cell_index in range(len(self.board)):
            self.board[cell_index].set_state(int(boardstr[cell_index]))



if __name__ == "__main__":
    rules = RulesConway()
    board = Board(rules, 5, 5, "0001001010110011000100010")
    board.print_board()
    board.next_gen()
    board.print_board()
