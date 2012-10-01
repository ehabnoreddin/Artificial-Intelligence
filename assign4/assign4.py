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
from sys import exit                        # For bad import statements

###############################################################################
# Custom module import statements
###############################################################################

try:
    from gameSearch import negamax
    from ttt import TTT
except ImportError as ie:
    exit("Error while importing a required module ({}).".format(ie))

###############################################################################
###############################################################################

###############################################################################
# Functions and classes defined for this assignment
###############################################################################

debug = False

def playGameNegamax(game):
    '''The original game function given for the assignment with added code for
    displaying the move count once the game is over.'''
    
    print(game)
    while not game.isOver():
        value,move = negamax(game,9)
        if move == None :
            print("move is None. Stopping")
            break
        game.makeMove(move)
        print("Player",game.player,"to",move,"for value",value)
        if not debug: print()
        print(game)
        game.changePlayer()
        
    print('Number of moves explored: {}'.format(game.iMoveCount))


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
    
    print("Running main game..\n\n")

    playGameNegamax(TTT())
    
###############################################################################
###############################################################################
    
if __name__ == '__main__':
    main()