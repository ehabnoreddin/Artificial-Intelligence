#!/usr/bin/env python -O

'''
	File: 	        eightPuzzle.py
	Author:         Corey Prophitt <prophitt.corey@gmail.com>
	Class:	        CS440, Colorado State University.
	License:        GPLv3, see license.txt for more details.

        Description:
        
            A few solutions to the 8-puzzle. 
'''

###############################################################################
# Standard module import statements
###############################################################################

from __future__ import print_function
import copy
import search

###############################################################################
###############################################################################


###############################################################################
# Custom module import statements
###############################################################################

from search import ebf, iterativeDeepeningSearch, RBFS, getNodeCount, getNCount

###############################################################################
###############################################################################


###############################################################################
# Initial states and goals 
###############################################################################

# The start node used in the assignment
startState = [1,2,3, 4,0,5, 6,7,8]

# The three goal nodes used in the assignment
goalState =  [1,2,3, 4,0,5, 6,7,8]
goalState2 = [1,2,3, 4,5,8, 6,0,7]
goalState3 = [1,0,3, 4,5,8, 2,6,7]

###############################################################################
###############################################################################


###############################################################################
# Functions defined for the A* algorithm
###############################################################################

def manhattanDistance(x1, y1, x2, y2):
    '''Returns the 'Manhattan distance' from one point to another.'''
    return abs(x2 - x1) + abs(y2 - y1)

def h1(state, start=startState):
    '''Returns a constant cost of 0 for every state.'''
    return 0

def h2b(state, start=startState):
    '''Returns the traditional 'Manhattan distance' cost from the startState
    to the state.'''
         
    startRC = iTorc(start.index(0))
    goalRC = iTorc(state.index(0))
        
    return manhattanDistance(startRC[0], startRC[1], goalRC[0], goalRC[1])
       
def h2(state, start=startState):
    '''Returns the 'Manhattan distance' cost from the startState to the
    state. Often used in 8-puzzles.'''
    
    totalSum = 0    
    for i in range(len(state)):
        totalSum += h2(state, start)
        
    return totalSum       
        
def h3(state, start=startState):
    '''A custom implementation that is admissible. This function determines
    how many tiles in the state are different than those in the start state.
    This means if the start is the goal the difference is zero. The
    function can return up to 9 if every tile is different.'''
    
    moved = 0
    for i in range(len(state)):
        if state[i] != start[i]:
            moved = moved + 1
            
    return moved

def h4(state):
    '''
    '''

    totalSum = 0    
    for i in range(len(state)):
        totalSum += abs(startState.index(state[i]) - i)
        
    return totalSum

###############################################################################
###############################################################################


###############################################################################
# Functions common between the two algorithms and/or puzzle problem
###############################################################################

#
# Wrote by Chuck Anderson
#

def iTorc(i):
    '''Returns the (row,col) of the space at a given index.'''        
    row = i / 3
    col = i - row*3
    return (row, col)

def rcToi(row,col):
    return row*3+col

def setTile(state,row,col,tile):
    state[rcToi(row,col)] = tile
    return state

def getTile(state,row,col):
    return state[rcToi(row,col)]

def findBlank(s):
    return iTorc(s.index(0))

def actionsF(state):
    r,c = findBlank(state)
    actions = []
    if c > 0:
        actions.append("left")
    if c < 2:
        actions.append("right")
    if r > 0:
        actions.append("up")
    if r < 2:
        actions.append("down")
    return actions

def takeActionF(state,action):
    state = copy.deepcopy(state)
    r,c = findBlank(state)
    dr = dc = 0
    if action is "left":
        dc -= 1
    elif action is "right":
        dc += 1
    elif action is "up":
        dr -= 1
    elif action is "down":
        dr += 1
    newr, newc = r+dr, c+dc
    setTile(state,r,c,getTile(state,newr,newc))
    setTile(state,newr,newc,0)
    return state

#
# Wrote by me
#

def getIDSData(goal):
    res = iterativeDeepeningSearch(startState,actionsF,takeActionF, lambda (s): s==goal, 20)
    depth = len(res) - 1 # not counting start state..
    nodes = getNodeCount()
    branchf = ebf(nodes, depth)
    
    return depth, nodes, branchf

def getRBFSData(goal, hfunc):
    def goalTest(state):
        return state == goal
    
    def takeAction(state, action):
        return takeActionF(state, action), 1
    
    res = RBFS(startState, actionsF, takeAction, goalTest, hfunc)
    depth = len(res[0]) - 1 # not counting start state..
    nodes = getNCount()
    branchf = ebf(nodes, depth)
    
    return depth, nodes, branchf

def main():

    print("Warning: This file's hash-bang is set to run in Python's optimized mode..")
    print("Warning: This may take a while..output is done at the very end.\n")

    mformat = '''
            {}    {}    {} 
Algorithm    Depth  Nodes       EBF              Depth  Nodes       EBF              Depth  Nodes       EBF          
     IDS       {}      {}       {:.3f}              {}      {}      {:.3f}              {}      {}      {:.3f}         
    A*h1       {}      {}       {:.3f}              {}      {}      {:.3f}              {}      {}      {:.3f}
    A*h2       {}      {}       {:.3f}              {}      {}      {:.3f}              {}      {}      {:.3f}
    A*h3       {}      {}       {:.3f}              {}      {}      {:.3f}              {}      {}      {:.3f}   
'''

    # IDS results
    print("Finding IDS for goal 1")
    ids1 = getIDSData(goalState)
    print("Finding IDS for goal 2")
    ids2 = getIDSData(goalState2)
    print("Finding IDS for goal 3")
    ids3 = getIDSData(goalState3)
    #ids3 = 0, 0, 0  # speed up testing

    # H1 results
    print("Finding RBFS for goal 1, h1")
    rbfs1 = getRBFSData(goalState, h1)
    print("Finding RBFS for goal 2, h1")
    rbfs2 = getRBFSData(goalState2, h1)
    print("Finding RBFS for goal 3, h1")
    rbfs3 = getRBFSData(goalState3, h1)
    #rbfs3 = (0,0,0) #speed up testing        

    # H2 results
    print("Finding RBFS for goal 1, h2")
    rbfs4 = getRBFSData(goalState, h2)
    print("Finding RBFS for goal 2, h2")
    rbfs5 = getRBFSData(goalState2, h2)
    print("Finding RBFS for goal 3, h2")
    rbfs6 = getRBFSData(goalState3, h2)
    #rbfs6 = (0,0,0) #speed up testing
    
    # H3 results
    print("Finding RBFS for goal 1, h3")
    rbfs7 = getRBFSData(goalState, h3)
    print("Finding RBFS for goal 2, h3")
    rbfs8 = getRBFSData(goalState2, h3)
    print("Finding RBFS for goal 3, h3")
    rbfs9 = getRBFSData(goalState3, h3)
    #rbfs9 = (0,0,0) #speed up testing  
 
    mformat = mformat.format(goalState,
                             goalState2,
                             goalState3,
                             # IDS
                             ids1[0], ids1[1], ids1[2],
                             ids2[0], ids2[1], ids2[2],
                             ids3[0], ids3[1], ids3[2],
                             # H1
                             rbfs1[0], rbfs1[1], rbfs1[2],
                             rbfs2[0], rbfs2[1], rbfs2[2],
                             rbfs3[0], rbfs3[1], rbfs3[2],
                             # H2
                             rbfs4[0], rbfs4[1], rbfs4[2],
                             rbfs5[0], rbfs5[1], rbfs5[2],
                             rbfs6[0], rbfs6[1], rbfs6[2],
                             # H3
                             rbfs7[0], rbfs7[1], rbfs7[2],
                             rbfs8[0], rbfs8[1], rbfs8[2],
                             rbfs9[0], rbfs9[1], rbfs9[2])

    print(mformat)


###############################################################################
###############################################################################


if __name__ == "__main__":
    main()
