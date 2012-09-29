#!/usr/bin/env python

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

from search import ebf, iterativeDeepeningSearch, getNodeCount

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

def h2(state, start=startState):
    '''Returns the 'Manhattan distance' cost from the startState to the state.'''
         
    startRC = iTorc(start.index(0))
    goalRC = iTorc(state.index(0))
        
    return manhattanDistance(startRC[0], startRC[1], goalRC[0], goalRC[1])
        
def h3(state, start=startState):
    '''A custom implementation that is admissible. This function determines
    how many tiles in the state are different than those in the start state.
    This means if the start is the goal, the difference is zero, up to 9.'''
    
    moved = 0
    for i in range(len(state)):
        if state[i] != start[i]:
            moved = moved + 1
            
    return moved

###############################################################################
###############################################################################


###############################################################################
# Functions common between the two algorithms and/or puzzle problem
###############################################################################

#
# Wrote by Charles Anderson
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

def main():

    mformat = '''
            {}    {}    {} 
Algorithm    Depth  Nodes  EBF              Depth  Nodes  EBF              Depth  Nodes  EBF          
     IDS       {}      {}   {}                  {}     {}  {}                   {} {}  {}         
    A*h1       0      0  0.000                3    116  4.488               11 643246  3.263         
    A*h2       0      0  0.000                3     51  3.297               11 100046  2.733
    A*h2       0      0  0.000                3     51  3.297               11 100046  2.733
'''

    ids1 = getIDSData(goalState)
    ids2 = getIDSData(goalState2)
    #ids3 = getIDSData(goalState3)
    ids3 = 0, 0, 0  # speed up testing
    
    mformat = mformat.format(goalState,
                             goalState2,
                             goalState3,
                             ids1[0], ids1[1], ids1[2],
                             ids2[0], ids2[1], ids2[2],
                             ids3[0], ids3[1], ids3[2])

    print(mformat)


###############################################################################
###############################################################################


if __name__ == "__main__":
    main()
