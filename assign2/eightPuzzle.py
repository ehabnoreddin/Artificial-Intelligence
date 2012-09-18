#!/usr/bin/env python

'''
	File: 	        search.py
	Author:         Corey Prophitt <prophitt.corey@gmail.com>
	Class:	        CS440, Colorado State University.
	License:        GPLv3, see license.txt for more details.

        Description:
        
            The famous 8-puzzle solved using the iterative deepening algorithm.
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
    return "{0}{1}{2}\n{3}{4}{5}\n{6}{7}{8}".format(state[0],
                                                    state[1],
                                                    state[2],
                                                    state[3],
                                                    state[4],
                                                    state[5],
                                                    state[6],
                                                    state[7],
                                                    state[8],)
    
def actionsF(state):
    '''Returns a list of all possible actions from the current state. The input
    is the state, the output is a list of all possible actions from the given
    state. Returns an empty list if no action is possible.'''
    
    # Only test if the size is 9, and
    # if a zero (space) exists, else it's bad so return an empty list..
    if len(state) == 9 and 0 in state:
        zeroPos = state.index(0)
        if zeroPos == 0:
            return ['right', 'down']
        if zeroPos == 1:
            return ['left','right', 'down']
        if zeroPos == 2:
            return ['left', 'down']
        if zeroPos == 3:
            return ['right','up','down']
        if zeroPos == 4:
            return ['left','right','up', 'down']    
        if zeroPos == 5:
            return ['left','up','down']
        if zeroPos == 6:
            return ['right','up']
        if zeroPos == 7:
            return ['left','right','up']
        if zeroPos == 8:
            return ['left','up'] 
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
        state[zeroPos], state[zeroPos + 3] = state[zeroPos + 3], state[zeroPos]
        return state

    if action == 'up':
        state[zeroPos], state[zeroPos - 3] = state[zeroPos - 3], state[zeroPos]
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
    # Test printState as shown in class assignment details    
    state = [1, 0, 3, 4, 2, 5, 6, 7, 8]
    assert(printState(state) == "103\n425\n678")
    state = [1,2,3, 4,0,5, 6,7,8]
    assert(printState(state) == "123\n405\n678")
    
    # Test actionsF as shown in class assignment details
    assert(actionsF(state) == ['left', 'right', 'up', 'down'])
    state = [1,0,3, 4,2,5, 6,7,8]
    assert(actionsF(state) == ['left', 'right', 'down'])
    
    # Test takeActionF as shown in class assignment details
    state = [1,0,3, 4,2,5, 6,7,8]
    assert(takeActionF(copy(state), 'left') == [0,1,3, 4,2,5, 6,7,8])
    state = [1,0,3, 4,2,5, 6,7,8]
    assert(takeActionF(copy(state), 'right') == [1,3,0, 4,2,5, 6,7,8])
    state = [1,0,3, 4,2,5, 6,7,8]
    assert(takeActionF(copy(state), 'down') == [1,2,3, 4,0,5, 6,7,8])
    state = [1,2,3, 4,0,5, 6,7,8]
    assert(takeActionF(copy(state), 'up') == [1,0,3, 4,2,5, 6,7,8])
    
    # Setup a test state and goal
    start = [1,2,3, 4,0,5, 6,7,8]
    goal =  [1,2,3, 4,5,8, 6,0,7]
    def goalTestF(state):
        return state == goal

    # Test printing a solution path
    solution = search.iterativeDeepeningSearch(start, actionsF,
                                               takeActionF, goalTestF, 2)
    printResult(start, goal, solution)
        