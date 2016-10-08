#!/usr/bin/env python3
#
# Rulesets for cellular automata.
#

from utils import *

class RulesConway:
    state_dead = 0
    state_alive = 1

    """Ruleset for Conway's Game of Life."""
    def get_base_state(self):
        """Return the 'base state' for the ruleset.

        In Conway's Game of Life, that's 0 (dead)."""
        return RulesConway.state_dead

    def get_cell_next(self, cur_cell, neighbours):
        """Return the next state for the given cell, applying rules depending on
        the neighbours' states."""
        # get number of alive adjacent cells
        num_alive = 0
        for c in neighbours:
            if c.get_state() == RulesConway.state_alive:
                num_alive += 1

        ## apply rules for Conway's Game of Life {{{
        if cur_cell.get_state() == RulesConway.state_alive:
            # 1. Live cell, fewer than 2 live neighbours -> dead
            if num_alive < 2:
                return RulesConway.state_dead
            # 2. Live cell, 2 or 3 live neighbours -> live
            if num_alive == 2 or num_alive == 3:
                return RulesConway.state_alive
            # 3. Live cell, more than 3 live neighbours -> dead
            if num_alive > 3:
                return RulesConway.state_dead
        elif cur_cell.get_state() == RulesConway.state_dead:
            # 4. Dead cell, exactly 3 live neighbours -> live
            if num_alive == 3:
                return RulesConway.state_alive
            else:
                return RulesConway.state_dead
        ## }}}



if __name__ == "__main__":
    logging.error("This class cannot be run directly.")
    sys.exit(1)
