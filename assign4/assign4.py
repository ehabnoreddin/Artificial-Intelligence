#!/usr/bin/env python -O

'''
	File: 	        assign4.py
	Author:         Corey Prophitt <prophitt.corey@gmail.com>
	Class:	        CS440, Colorado State University.
	License:        GPLv3, see license.txt for more details.

        Description:
        
            Assignment 4 for CS440. Negamax with alpha-beta prunning applied
            to Tic-Tac-Toe.
'''

###############################################################################
# Standard module import statements
###############################################################################

from __future__ import print_function       # Let's keep Python 3 in mind
from random import shuffle                  # For the extra credit function

###############################################################################
# Custom module import statements
###############################################################################


###############################################################################
###############################################################################


###############################################################################
# Functions defined for this assignment
###############################################################################

def opponent(board, target=' '):
    '''Returns the index of the target in the board if one exists. Returns -1
    if the target is no where to be found in the board.'''
    return board.index(target) if target in board else -1
    
# Extra credit - A random opponent function
def opponentRandom(board, target=' '):
    '''Returns a random index of a target on the board. If the target does
    not exist on the board then -1 is returned.'''
    
    boardSize = len(board)
    moves = []
    for i in xrange(boardSize):
        if board[i] == target:
            moves.append(i)
    shuffle(moves)
    return moves.pop() if moves else -1
  
def main():
    '''The primary assignment functionality.'''
    print("Running main..\n\n")

def tests():
    '''A suite of tests for assign4.py functions.'''
    print("Running tests..\n\n")

###############################################################################
###############################################################################

    
if __name__ == '__main__':
    if __debug__:
        tests()
    main()