#!/usr/bin/env python

'''
	File: 	        testSecondPuzzle.py
	Author:         Corey Prophitt <prophitt.corey@gmail.com>
	Class:	        CS440, Colorado State University.
	License:        GPLv3, see license.txt for more details.

        Description:
        
            Testing the iterative deepening search on a second puzzle. The
            second puzzle I chose was a 3-puzzle. It's similar, simpler and
            was easier to test on. Plus, I used the 3-puzzle in my first
            assignment and I wanted to see the new algorithm work on it. The
            first time I completed the assignment I used a brute force method.
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
    '''Prints the solution path in a pretty format.
    '''
    print("Path from ")
    print(printState(startState))
    print("  to")
    print(printState(goalState))
    if solutionPath == "cutoff" or solutionPath == "failure":
        print("The path is {0}".format(solutionPath))
        return
    print("  is {0} node(s) long:".format(len(solutionPath)))
    for state in solutionPath:
        print(printState(state) + "\n")



if __name__ == '__main__':
    # Test printState  
    state = [0, 1, 2, 3]
    assert(printState(state) == "01\n23")
    state = [1, 0, 2, 3]
    assert(printState(state) == "10\n23")
    
    # Test actionsF 
    assert(actionsF(state) == ['left', 'down'])
    state = [2, 1, 0, 3]
    assert(actionsF(state) == ['right', 'up'])
    
    # Test takeActionF 
    assert(takeActionF(copy(state), 'right') == [2, 1, 3, 0])
    assert(takeActionF(copy(state), 'up') == [0, 1, 2, 3])
    
    # Setup a test state and goal
    start = [0, 1, 2, 3]
    goal =  [1, 3, 0, 2]
    def goalTestF(state):
        return state == goal

    # Test printing a solution path
    solution = search.iterativeDeepeningSearch(start, actionsF,
                                               takeActionF, goalTestF, 6)
    printResult(start, goal, solution)