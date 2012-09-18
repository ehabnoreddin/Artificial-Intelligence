#!/usr/bin/env python

'''
	File: 	        testSecondPuzzle.py
	Author:         Corey Prophitt <prophitt.corey@gmail.com>
	Class:	        CS440, Colorado State University.
	License:        GPLv3, see license.txt for more details.

        Description:
        
            Testing the iterative deepening search on a second puzzle. The
            second puzzle I chose was a 3-puzzle. It's similar, simpler and
            was easier to test on. 
'''

#
# Standard module imports
#
from copy import copy

#
# Custom module imports
#
import search


def printState(state):
    '''Prints a state in a more human friendly way.'''
    return "{0}{1}\n{2}{3}".format(state[0], state[1], state[2], state[3])
    
def actionsF(state):
    '''Returns a list of all possible actions from the current state. The input
    is the state, the output is a list of all possible actions from the given
    state. Returns an empty list if no action is possible.'''
    
    # Only test if the size is 4, and
    # if a zero (space) exists, else it's bad so return an empty list..
    if len(state) == 4 and 0 in state:
        zeroPos = state.index(0)
        if zeroPos == 0:
            return ['right', 'down']
        if zeroPos == 1:
            return ['left', 'down']
        if zeroPos == 2:
            return ['right', 'up']
        if zeroPos == 3:
            return ['left', 'up']
    return []
    
    
def takeActionF(state, action):
    '''Takes an action and performs that on the given state. Possible actions
    include 'up' ,'down', 'left' and 'right'. These move the space around the
    puzzle board. The output is the new state which is a result of the action.
    '''
    
    actions = actionsF(state)
    if action not in actions:
        # Returns an empty list, action requested was impossible..
        return []
        
    zeroPos = state.index(0)
    if action == 'left':
        state[zeroPos], state[zeroPos - 1] = state[zeroPos - 1], state[zeroPos]
        return state
    
    if action == 'right':
        state[zeroPos], state[zeroPos + 1] = state[zeroPos + 1], state[zeroPos]
        return state
    
    if action == 'down':
        state[zeroPos], state[zeroPos + 2] = state[zeroPos + 2], state[zeroPos]
        return state

    if action == 'up':
        state[zeroPos], state[zeroPos - 2] = state[zeroPos - 2], state[zeroPos]
        return state
    
    return []


def printResult(startState, goalState, solutionPath):
    print("Path from ")
    print(printState(startState))
    print("  to")
    print(printState(goalState))
    print("  is {0} nodes long:", len(solutionPath))
    for state in solutionPath:
        print(printState(state + "\n"))



if __name__ == '__main__':
    pass