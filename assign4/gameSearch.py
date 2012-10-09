#!/usr/bin/env python 

'''
	File: 	        gameSearch.py
	Author:         Corey Prophitt <prophitt.corey@gmail.com>
	Class:	        CS440, Colorado State University.
	License:        GPLv3, see license.txt for more details.

        Description:
        
            Negamax with alpha-beta prunning.
'''

###############################################################################
# Standard module import statements
###############################################################################

from __future__ import print_function       # Let's keep Python 3 in mind
from sys import exit                        # For bad import statements

###############################################################################
# Custom module import statements
###############################################################################

try:
    pass
except ImportError as ie:
    exit("Error while importing a required module ({}).".format(ie))

###############################################################################
###############################################################################

###############################################################################
# Functions and classes defined for searching within games
###############################################################################

### Assumes that the argument 'game' is an object with the following methods
# game.getMoves()
# game.makeMove(move)    changes lookahead player
# game.unmakeMove(move)  changes lookahead player
# game.changePlayer()    changes next turn player
# game.getUtility()
# game.isOver()
# game.__str__()

debug = False
inf = float('infinity')

def negamax(game, depthLeft):
    if debug: print('   '*(10-depthLeft), game)
    # If at terminal state or depth limit, return utility value and move None
    if game.isOver() or depthLeft == 0:
        if debug: print('terminal value',game.getUtility())
        return game.getUtility(), None
    if debug: print
    # Find best move and its value from current state
    bestValue = -inf
    bestMove = None
    for move in game.getMoves():
        # Apply a move to current state
        game.makeMove(move)
        # Use depth-first search to find eventual utility value and back it up.
        #  Negate it because it will come back in context of next player
        value = - negamax(game,depthLeft-1)[0]
        # Remove the move from current state, to prepare for trying a different move
        game.unmakeMove(move)
        if debug: print('   '*(10-depthLeft), game, "move",move,"backed up value",value)
        if value > bestValue:
            # Value for this move is better than moves tried so far from this state.
            bestValue = value
            bestMove = move
            if debug: print("new best")
        else:
            if debug: print()
    return bestValue, bestMove

COUNT = 0

def getCount():
    global COUNT
    tmp = COUNT
    COUNT = 0
    return tmp

def incCount():
    global COUNT
    COUNT = COUNT + 1

def negamaxIDS(game, depthLeft, ab=False):
    '''Negamax done using IDS.'''
    if debug: print('   '*(10-depthLeft), game)
    # If at terminal state or depth limit, return utility value and move None
    if game.isOver() or depthLeft == 0:
        if debug: print('terminal value',game.getUtility())
        return game.getUtility(), None
    if debug: print
    # Find best move and its value from current state
    bestValue = -inf
    bestMove = None

    for move in game.getMoves():
	incCount()	
	
        # Apply a move to current state
        game.makeMove(move)
        # Use depth-first search to find eventual utility value and back it up.
       
        value = negamaxIDS(game,depthLeft-1)
	
	 #  Negate it because it will come back in context of next player
	if value is not None:
	    value = - max(value)
	    
        # Remove the move from current state, to prepare for trying a different move
        game.unmakeMove(move)
        if debug: print('   '*(10-depthLeft), game, "move",move,"backed up value",value)
        if value > bestValue:
            # Value for this move is better than moves tried so far from this state.
            bestValue = value
            bestMove = move
	    # Alpha-beta prunning, take the best we've got..	    
	    if ab:
		return bestValue, bestMove
            if debug: print("new best")
        else:
            if debug: print()
    return bestValue, bestMove

def negamaxIDSab(game, depthLeft):
    '''Negamax with alphabeta prunning enabled.. I made this because the assignment
    asked for a new function, however the main functionality is done in the IDS
    function above.'''
    return negamaxIDS(game, depthLeft, True)

def ebf(numberOfMoves, depth):
    '''Returns an estimate of the estimated branching factor for a given number of
    moves and depth. If the depth is 0 then the EBF is 0.000.'''
    return numberOfMoves**(1.0/depth) if depth > 0 else 0.000


###############################################################################
###############################################################################


if __name__ == '__main__':
    pass