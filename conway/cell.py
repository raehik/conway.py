#!/usr/bin/env python3
#
# A cellular automaton cell able to hold an arbitrary number of states.
#

from utils import *

class Cell:
    """A cellular automaton cell able to hold an arbitrary number of states."""
    def __init__(self, begin_state=0):
        """Initialise cell. If an argument is given, set cell's state to it."""
        self.set_state(begin_state)

    def set_state(self, state):
        """Set cell's state to an integer value.

        This is not constrained in any way (TODO: should I allow -ve states
        though?), as the Board and RuleSet should handle that for each Cell.
        """
        self.state = state

    def get_state(self):
        """Retrieve the cell's current state."""
        return self.state



if __name__ == "__main__":
    logging.error("This class cannot be run directly.")
    sys.exit(1)
