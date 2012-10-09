#!/usr/bin/env python 

'''
	File: 	        ttt.py
	Author:         Corey Prophitt <prophitt.corey@gmail.com>
	Class:	        CS440, Colorado State University.
	License:        GPLv3, see license.txt for more details.

        Description:
        
            A Tic-Tac-Toe game. 
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
# Functions and classes defined for Tic-Tac-Toe
###############################################################################

class TTT:

    def __init__(self,debug=False):
        self.debug = debug
        self.iMoveCount = 0
        self.winner = None
        self.board =  [' ']*9
        self.player = 'X'
        if False:
            self.board = ['X','X',' ',
			  'X','O','O',
			  ' ',' ',' ']
            self.player = 'O'
        self.playerLookAHead = self.player

    def locations(self,c):
        return filter(lambda i: self.board[i] == c, range(len(self.board)))

    def getMoves(self):
        moves = self.locations(' ')
        return moves
        
    def getUtility(self):
        whereX = self.locations('X')
        whereO = self.locations('O')
        wins = [[0,1,2],[3,4,5],[6,7,8],
                [0,3,6],[1,4,7],[2,5,8],
                [0,4,8],[2,4,6]]
        isXWon = any([all([wi in whereX for wi in w]) for w in wins])
        isOWon = any([all([wi in whereO for wi in w]) for w in wins])
        if isXWon:
            self.winner = 'X'
            return 1 if self.playerLookAHead is 'X' else -1
        elif isOWon:
            self.winner = 'O'
            return 1 if self.playerLookAHead is 'O' else -1
        elif ' ' not in self.board:
            self.winner = 'Tie'
            return 0
        else:
            return None
            
    def isOver(self):
        return self.getUtility() != None

    def makeMove(self,move):
        self.iMoveCount = self.iMoveCount + 1
        self.board[move] = self.playerLookAHead
        self.playerLookAHead = 'X' if self.playerLookAHead=='O' else 'O'

    def changePlayer(self):
        self.player = 'X' if self.player=='O' else 'O'
        self.playerLookAHead = self.player

    def unmakeMove(self,move):
        self.board[move] = ' '
        self.playerLookAHead = 'X' if self.playerLookAHead=='O' else 'O'

    def __str__(self):
        if self.debug:
            s = "|%c%c%c|%c%c%c|%c%c%c|" % tuple(self.board)
        else:
            s = "%c|%c|%c\n-----\n%c|%c|%c\n-----\n%c|%c|%c" % tuple(self.board)
        return s

###############################################################################
###############################################################################


if __name__ == '__main__':
    pass