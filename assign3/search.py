#!/usr/bin/env python

'''
	File: 	        search.py
	Author:         Corey Prophitt <prophitt.corey@gmail.com>
	Class:	        CS440, Colorado State University.
	License:        GPLv3, see license.txt for more details.

        Description:
        
            RBFS search algorithm and the IDS search algorithms.
'''

###############################################################################
# The IDS search algorithm (provided by Chuck Anderson) and modified by me
###############################################################################

COUNT = 0

def incCount():
    global COUNT
    COUNT = COUNT + 1
    
def getNodeCount():
    global COUNT
    tmp = COUNT
    COUNT = 0
    return tmp

def iterativeDeepeningSearch(startState, actionsF, takeActionF, goalTestF, maxDepth):
    startState
    for depth in range(maxDepth):
        result = depthLimitedSearchHelper(startState,actionsF,takeActionF,goalTestF,depth)
        if result is not "cutoff":
            result.insert(0,startState)
            return result
    return "cutoff"

def depthLimitedSearchHelper(state, actionsF, takeActionF, goalTestF, depthLimit):
    if goalTestF(state): 
        return [] 
    if depthLimit == 0:
        return "cutoff"
    cutoffOccurred = False
    for action in actionsF(state):
        childState = takeActionF(state,action)
	incCount()
        result = depthLimitedSearchHelper(childState,actionsF,takeActionF,goalTestF, depthLimit-1)
        if result is "cutoff":
            cutoffOccurred = True
        elif result is not "failure":
            result.insert(0,childState)
            return result
    if cutoffOccurred:
        return "cutoff"

###############################################################################
###############################################################################


###############################################################################
# The RBFS algorithm (provided in class notes) and modified by me
###############################################################################

NCOUNT = 0

def getNCount():
    global NCOUNT
    tmp = NCOUNT
    NCOUNT = 0
    return tmp

class Node:
    def __init__(self, state, f=0, g=0 ,h=0):
        self.state = state
        self.f = f
        self.g = g
        self.h = h
    def __repr__(self):
        return "Node(" + repr(self.state) + ", f=" + repr(self.f) + \
               ", g=" + repr(self.g) + ", h=" + repr(self.h) + ")"

def RBFS(startState, actionsF, takeActionF, goalTestF, hF):
    h = hF(startState)
    startNode = Node(state=startState, f=0+h, g=0, h=h)
    return RBFSHelper(startNode, actionsF, takeActionF, goalTestF, hF, float('inf'))

def RBFSHelper(parentNode, actionsF, takeActionF, goalTestF, hF, fmax):
    global NCOUNT
    if goalTestF(parentNode.state):
        return ([parentNode.state], parentNode.g)
    ## Construct list of children nodes with f, g, and h values
    actions = actionsF(parentNode.state)
    if not actions:
        return ("failure", float('inf'))
    children = []
    for action in actions:
        (childState,stepCost) = takeActionF(parentNode.state, action)
        h = hF(childState)
	NCOUNT += 1
        g = parentNode.g + stepCost
        f = max(h+g, parentNode.f)
        childNode = Node(state=childState, f=f, g=g, h=h)
        children.append(childNode)
    while True:
        # find best child
        children.sort(key = lambda n: n.f) # sort by f value
        bestChild = children[0]
        if bestChild.f > fmax:
            return ("failure",bestChild.f)
        # next lowest f value
        alternativef = children[1].f if len(children) > 1 else float('inf')
        # expand best child, reassign its f value to be returned value
        result,bestChild.f = RBFSHelper(bestChild, actionsF, takeActionF, goalTestF,
                                        hF, min(fmax,alternativef))
        if result is not "failure":               
            result.insert(0,parentNode.state)     
            return (result, bestChild.f)     

###############################################################################
###############################################################################


###############################################################################
# Functions common between the algorithms
###############################################################################

def ebf(numberNodes, depth, precision=0.01):
    if depth == 0:
	return 0.000
    return numberNodes**(1.0/depth)

###############################################################################
###############################################################################


if __name__ == "__main__":
    pass