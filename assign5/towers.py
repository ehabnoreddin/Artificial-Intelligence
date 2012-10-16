#!/usr/bin/env python -O

'''
	File: 	        towers.py
	Author:         Corey Prophitt
	License:        GPLv3, see license.txt for more details.

    Description:
        Homework assignment 5 for CSU's CS440.
'''

###############################################################################
# Standard module import statements
###############################################################################

try:
    import numpy as np
    #import matplotlib.pyplot as plt # not working on OSX
except ImportError as ie:
    print("Error while importing required files ({}).".format(ie))

from random import choice
from copy import copy

###############################################################################
###############################################################################

# incomplete state transitions, should be 21 or so in total.
state_transitions = {
    (1,0,0, 2,0,0, 3,0,0) : [[0,0,0, 2,0,0, 3,1,0], [0,0,0, 2,0,0, 3,0,1]],
    (0,0,0, 2,0,0, 3,1,0) : [[0,0,0, 0,0,0, 3,1,2], [0,0,0, 0,2,0, 3,1,0]],
    (0,0,0, 2,0,0, 3,0,1) : [[0,0,0, 0,0,0, 3,2,1], [1,0,0, 2,0,0, 3,0,0]],
    (0,0,0, 0,0,0, 3,1,2) : [[0,0,0, 0,0,1, 3,0,2], [0,0,0, 1,0,0, 3,0,2]],
    (0,0,0, 0,0,0, 3,2,1) : [[0,0,0, 0,1,0, 3,2,0], [0,0,0, 2,0,0, 3,0,1]],
    (0,0,0, 0,0,1, 3,0,2) : [[0,0,0, 0,0,1, 0,3,2], [0,0,0, 0,0,0, 3,1,2]],
    (0,0,0, 0,1,0, 3,2,0) : [[0,0,0, 0,1,0, 0,2,3], [0,0,0, 0,0,0, 3,2,1]],
    (0,0,0, 0,0,1, 0,3,2) : [[0,0,0, 0,0,0, 1,3,2], [0,0,0, 0,1,0, 0,3,2]],
    (0,0,0, 0,1,0, 0,2,3) : [[0,0,0, 0,0,0, 1,2,3], [0,0,0, 0,0,1, 0,2,3]],
    (0,0,0, 0,0,0, 1,3,2) : [[0,0,0, 0,1,0, 0,3,2], [0,0,0, 0,0,1, 0,3,2]],
    (0,0,0, 0,1,0, 0,3,2) : [[0,0,0, 0,0,0, 1,3,2], [0,0,0, 0,0,1, 0,3,2]],
    (0,0,0, 0,2,0, 3,1,0) : [[0,0,0, 0,2,0, 0,1,3], [0,0,0, 0,0,0, 3,1,2]],
    (0,0,0, 0,2,0, 0,1,3) : [[0,0,0, 0,0,2, 0,1,3], [0,0,0, 0,0,0, 2,1,3]],
    (0,0,0, 0,0,2, 0,1,3) : [[0,0,1, 0,0,2, 0,0,3], [0,0,0, 0,0,2, 1,0,3]],
}


def foundGoal(board):
    return board == [0,0,1, 0,0,2, 0,0,3]

def printPegs(state):
    pegs = '''
        %d %d %d
        %d %d %d
        %d %d %d
        =====
    '''
    return pegs % tuple(state)

def getMoves(board):
    global state_transitions
    return state_transitions[tuple(board)]

nGames = 1                              # number of games
rho = 0.1                               # learning rate
epsilonExp = 0.999                      # rate of epsilon decay
Q = {}                                  # initialize Q dictionary
epsilon = 1.0                           # initial epsilon value
showMoves = True                        # flag to print each board change

for game in range(nGames):              # iterate over multiple games

    epsilon *= epsilonExp
    step = 0
    board = [1,0,0, 2,0,0, 3,0,0]
    done = False

    while not done:
        step += 1

        printPegs(board)

        validMoves = getMoves(board)
        if np.random.uniform() < epsilon:
            move = choice(validMoves)       # Randomly chooses list item
        else:
            # Greedy move. Collect Q values for valid moves from current board.
            # Select move with highest Q value
            qs = []
            for m in validMoves:
                qs.append(Q.get((tuple(board), tuple(m)), -1))
            move = validMoves[np.argmax(np.asarray(qs))]

        printPegs(move)

        key = (tuple(board), tuple(move))

        if key not in Q:
            Q[(tuple(board), tuple(move))] = -1

        # CHANGE
        boardNew = copy(move)

        if showMoves:
            printPegs(boardNew)

        if foundGoal(boardNew):
            Q[(tuple(board), tuple(move))] = 0
            done = True

        if step > 1:
            Q[(tuple(boardOld), tuple(moveOld))] += rho * (Q[(tuple(board), tuple(move))] - Q[(tuple(boardOld), tuple(moveOld))])

        boardOld,moveOld = board,move
        board = boardNew
