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
    from gameSearch import ebf, negamax, negamaxIDS, negamaxIDSab
    from ttt import TTT
except ImportError as ie:
    exit("Error while importing a required module ({}).".format(ie))

###############################################################################
###############################################################################

###############################################################################
# Functions and classes defined for this assignment
###############################################################################

debug = False


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

def playGameNegamax(game, IDS=False, ab=False):
    '''The original game function given for the assignment with added code for
    displaying the move count once the game is over.'''
    
    print(game)
    value = 0
    turns = 0
    
    while not game.isOver():
	if game.player == 'X':
		turns = turns + 1
	if not IDS and game.player == 'X':
	    value,move = negamax(game,9)
	else:
	    if not ab and game.player == 'X':
		value,move = negamaxIDS(game, 9, ab = False)
	    else:
		if game.player == 'X':
		    value,move = negamaxIDS(game, 9, ab = True)
		else:
		    # This is the 'stupid' opponent
		    move = opponent(game.board)
		
        if move == None :
            print("move is None. Stopping")
            break
        game.makeMove(move)
        print("Player",game.player,"to",move,"for value",value)
        if not debug: print()
        print(game)
        game.changePlayer()

    movesCount = '{} moves explored '.format(game.iMoveCount)
    ebfValue = 'for an ebf of {:.3f}'.format(ebf(game.iMoveCount, turns))
    mebf = 'alpha-beta prunning, ' + movesCount + ebfValue + '.'
    
    print('\nWith ' + mebf if ab else '\nWithout ' + mebf)
    print()
    
def playGameNegamaxMultipleRounds(rounds=100):
    '''Extra credit problem-- 100 games, average win ratio for 'X'. I used
    negamaxIDS with alpha-beta prunning because it's faster (but less effective
    sometimes). Can specify any number of rounds..'''
    
    print("Playing {} games and finding average # of 'X' wins.".format(rounds))
    
    xWins = 0
    value = 0
    
    for round in range(rounds):
	game = TTT(False)
	print(game)
	while not game.isOver():
	    if game.player == 'X':
		value,move = negamaxIDS(game, 9, ab = True)
	    else:
		move = opponentRandom(game.board)
	    if move == None:
		print("move is None. Stopping")
		break
	    game.makeMove(move)
	    print("Player",game.player,"to",move,"for value",value)
	    if not debug: print()
	    print(game)
	    game.changePlayer()
	if game.winner == 'X':
	    xWins = xWins + 1
        
    msg = "'X' won {0} out of {1} games for {2}% wins.".format(xWins, rounds, (xWins/rounds) * 100)    
    print(msg)
  
def main():
    '''The primary assignment functionality.'''
    
    print("Running main game..\n\n")
    
    # Play with with negamaxIDS
    playGameNegamax(TTT(False), IDS = True, ab = False)
    
    # Play with negamaxIDSab
    playGameNegamax(TTT(False), IDS = True, ab = True)
    
    # Extra credit problem 2
    #playGameNegamaxMultipleRounds(100)
    
###############################################################################
###############################################################################
    
if __name__ == '__main__':
    main()