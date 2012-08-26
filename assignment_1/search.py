#!/usr/bin/env python

'''
	File: 	    search.py
	Author:     Corey Prophitt <prophitt.corey@gmail.com>
	Class:	    CS440
	License:    GPLv3, see license.txt for more details.
'''


#
# The graph search algorithms (BFS, DFS)
#

def breadthFirstSearch(startState, goalState, successorsf):
    '''
    Performs a breadth first search traveral on a graph.

    Input:
        A 'startState', a 'goalState' and a successors function.
    Output:
        A list representing the path from the startState to the goalState.
        Returns an empty list if a path doesn't exist.
    '''
    
    
    # A few checks up top, easy/quick bail outs
    if startState == goalState:
        return [startState]
    
    if successorsf(startState) is None:
        return []
    
    if successorsf(startState) is []:
        return []
    
    # Traverse the graph
    queue = []
    queue.append([startState])
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == goalState:
            return path
            
        for childNode in successorsf(node):
            newPath = list(path)
            newPath.append(childNode)
            queue.append(newPath)
            
    return []
            

def depthFirstSearch(startState, goalState, successorsf):
    '''
    Performs a depth first search traveral on a graph.

    Input:
        A 'startState', a 'goalState' and a successors function.
    Output:
        A list representing the path from the startState to the goalState.
        Returns an empty list if a path doesn't exist.
    '''
    
    pass


#
# Main
#

if __name__ == '__main__':

    #
    # We don't need to run this as main. Since the successorsf is defined
    # in simpleGraph, I will run all tests of these functions in that module.
    #
    
    pass
