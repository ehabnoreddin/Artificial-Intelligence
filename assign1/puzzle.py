#!/usr/bin/env python

'''
	File: 	        puzzle.py
	Author:         Corey Prophitt <prophitt.corey@gmail.com>
	Class:	        CS440, Colorado State University.
	License:        GPLv3, see license.txt for more details.

        Description:
        
            The puzzle I chose to do was the (2x2) '3' sliding puzzle. This is
	    easily represented as a graph and transitions are very simple. 
'''

#
# Custom Module Imports
#

from search import breadthFirstSearch, depthFirstSearch


def successorsf(gameState):
    '''
    Input:
        Takes in a game state as a string 'A' -> 'L'. 
        
    Output:
        Returns a list of possible transitions from that state.

        Returns an empty list if no transitions are possible or if the state
        does not exist.
    
    '''
    
    if gameState is None or not isinstance(gameState, str):
        return []
        
    if gameState not in states:
        return []
        
    return state_transitions[gameState]


#
# A board state, useful for printing a pretty path later! 
#

class State:
    def __init__(self, p1, p2, p3, p4):
        '''
        Initialize a "State" with four numbers. The zero represents the space
        on the board. The numbers one, two and three represent the other board
        tiles. Or you can use whatever numbers you want.. 
        '''
        
        self.p1 = p1; self.p2 = p2
        self.p3 = p3; self.p4 = p4
        
    def __str__(self):
        '''
        Turns a State object into a pretty little string representing the state.
        '''
        
        wall = "+---+"
        return "{0}\n|{1}|{2}|\n|{3}|{4}|\n{5}".format(wall,
                                                       self.p1,
                                                       self.p2,
                                                       self.p3,
                                                       self.p4,
                                                       wall)


def printStates(listOfStates):
    '''
    A quick and dirty function to print the list of states in a more human
    friendly manner.
    '''
    
    if len(listOfStates) == 0:
        print "No path exists!"
        return
        
    for i in range(0, len(listOfStates) - 1):
        print states[listOfStates[i]]
        print "  |\n  |\n  V"
    print states[listOfStates[-1]]


#
# The possible states for the puzzle. There are a total of 4! / 2 total valid
# states for this puzzle, therefore there are 12 states. 
#

states = {
    'A' : State(0, 1, 3, 2),
    'B' : State(3, 1, 0, 2),    
    'C' : State(3, 1, 2, 0),   
    'D' : State(3, 0, 2, 1),   
    'E' : State(0, 3, 2, 1),    
    'F' : State(2, 3, 0, 1),    
    'G' : State(2, 3, 1, 0),
    'H' : State(2, 0, 1, 3),
    'I' : State(0, 2, 1, 3),
    'J' : State(1, 2, 3, 0),
    'K' : State(1, 2, 3, 0),
    'L' : State(1, 0, 3, 2)
}

#
# The possible state transitions. There are always two ways to move per-state.
# This means there are 12*2 possible transitions for a total of 24 transitions.
# The following graph depicts all 24 transitions.
#

state_transitions = {
    'A' : ['L','B'],
    'B' : ['A','C'],
    'C' : ['B','D'],
    'D' : ['C','E'],
    'E' : ['D','F'],
    'F' : ['E','G'],
    'G' : ['F','H'],
    'H' : ['G','I'],
    'I' : ['H','J'],
    'J' : ['I','K'],
    'K' : ['J','L'],
    'L' : ['K','A'] 
}


if __name__ == '__main__':

    #
    # A few examples of finding paths through the puzzle using BFS and DFS.
    #
    
    print("From NotInGraph to 'L'")    
    printStates(depthFirstSearch('NotInGraph', 'G', successorsf))
    
    print("\nFrom A to G (DFS): ")
    printStates(depthFirstSearch('A', 'G', successorsf))
    
    print("\nFrom A to E (BFS): ")
    printStates(breadthFirstSearch('A', 'E', successorsf))
    
        
    