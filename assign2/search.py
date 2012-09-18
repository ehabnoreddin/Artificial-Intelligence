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
# The example graph given in the assignment description.
#

successors = {
    'a':  ['b', 'c', 'd'],
    'b':  ['e', 'f', 'g'],
    'c':  ['a', 'h', 'i'],
    'd':  ['j', 'z'],
    'e':  ['k', 'l'],
    'g':  ['m'],
    'k':  ['z']
}


def iterativeDeepeningSearch(startState, actionsF, takeActionF, goalTestF, maxDepth):
    if goalTestF:
        return []
    if maxDepth == 0:
        return "cutoff"
    for action in actionsF():
        childState = takeActionF(startState, action)
        result = depthLimitedSearchHelper(childState, actionsF, takeActionF, goalTestF, maxDepth-1)
        if result is "cutoff":
            cutoffOccurred = True
        else:
            if result is not "failure":
                return result
    if cutoffOccurred:
        return "cutoff"
    else:
        return "failure"


def depthLimitedSearchHelper(state, actionsF, takeActionF, goalTestF, depthLimit) :
    for depth in range(maxDepth):
        result = depthLimitedSearchHelper(startState, actionsF, takeActionF, goalTestf, depth)
        if result is not "cutoff":     
            return result
    return "cutoff"

    
if __name__ == '__main__':
    pass