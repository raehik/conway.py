#!/usr/bin/env python3
#
# Rulesets for cellular automata.
#

from utils import *

class RulesConway:
    """Ruleset for Conway's Game of Life."""
    def get_base_state(self):
        """Return the 'base state' for the ruleset.

        In Conway's Game of Life, that's 0 (dead)."""
        return 0

    def get_cell_next(self, cell, neighbours):
        """Return the next state for the given cell, applying rules depending on
        the neighbours' states."""
        logging.debug("get_cell_next: TODO")
        return 0



if __name__ == "__main__":
    logging.error("This class cannot be run directly.")
    sys.exit(1)
