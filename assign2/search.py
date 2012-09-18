#!/usr/bin/env python

'''
	File: 	        search.py
	Author:         Corey Prophitt <prophitt.corey@gmail.com>
	Class:	        CS440, Colorado State University.
	License:        GPLv3, see license.txt for more details.

        Description:
        
            The iterative deepening search algorithm. 
'''

#
# Standard module imports
#
from copy import copy


def depthLimitedSearchHelper(state, actionsF, takeActionF, goalTestF, depthLimit):
    path = [state]
    if goalTestF(state):
        return state
    if depthLimit == 0:
        return "cutoff"
    for action in actionsF(state):
        childState = takeActionF(copy(state), action)
        result = depthLimitedSearchHelper(childState, actionsF, takeActionF, goalTestF, depthLimit-1)
        if result == "cutoff":
            cutoffOccurred = True
        else:
            if result != "failure":
                return path + result
    if cutoffOccurred:
        return "cutoff"
    else:
        return "failure"


def iterativeDeepeningSearch(startState, actionsF, takeActionF, goalTestF, maxDepth) :
    for depth in range(maxDepth):
        result = depthLimitedSearchHelper(startState, actionsF, takeActionF, goalTestF, depth)
        if result != "cutoff":     
            return startState + result
    return "cutoff"

    
if __name__ == '__main__':
    pass