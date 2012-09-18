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
    '''A helper function for the iterative deepening search. Does the recursive
    calls. This is almost verbatim from the class notes.
    '''
    
    if goalTestF(state):
        return state
    if depthLimit == 0:
        return "cutoff"
    for action in actionsF(state):
        childState = takeActionF(copy(state), action)
        result = depthLimitedSearchHelper(childState, actionsF, takeActionF, goalTestF, depthLimit-1)
        if result == "cutoff":
            cutoffOccurred = True
        elif result != "failure":
                return result
    if cutoffOccurred:
        return "cutoff"
    else:
        return "failure"


def iterativeDeepeningSearch(startState, actionsF, takeActionF, goalTestF, maxDepth):
    '''The iterative portion of the search. Iterates through the possible "depths".
    This is almost verbatim from the class notes.'''
    
    for depth in range(maxDepth):
        result = depthLimitedSearchHelper(startState, actionsF, takeActionF, goalTestF, maxDepth)
        if result != "cutoff":     
            return [result]
    return "cutoff"

    
if __name__ == '__main__':
    pass