#!/usr/bin/env python

'''
	File: 	    search.py
	Author:     Corey Prophitt <prophitt.corey@gmail.com>
	Class:	    CS440, Colorado State University.
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
    if not isinstance(startState, str):
        return []

    if not isinstance(goalState, str):
        return []

    if successorsf(startState) == []:
        return []
    
    if startState == goalState:
        return [startState]
    
    # Traverse the graph
    queue = [ [startState] ]
    visited = []
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node in visited:
            continue
        visited.append(node)
        
        if node == goalState:
            return path
            
        for childNode in successorsf(node):
            newPath = list(path)
            newPath.append(childNode)
            queue.append(newPath)

    # If we've gotten to this point, the path doesn't exist
    # so we return an empty list.
    return []
            

def depthFirstSearch(startState, goalState, successorsf, path=[]):
    '''
    Performs a depth first search traveral on a graph.

    Input:
        A 'startState', a 'goalState' and a successors function.
    Output:
        A list representing the path from the startState to the goalState.
        Returns an empty list if a path doesn't exist.
    '''

    if not isinstance(startState, str):
        return []

    if not isinstance(goalState, str):
        return []

    if path == [] and successorsf(startState) == []:
        return []  

    path = path + [startState]
    if startState == goalState:
        return path      

    if successorsf(startState) == []:
        return []
    
    for node in successorsf(startState):
        if node not in path:
            newPath = depthFirstSearch(node, goalState, successorsf, path)
            if newPath: 
                return newPath
        
    return []


#
# Main
#

if __name__ == '__main__':

    #
    # We don't need to run this as main. Since the successorsf is defined
    # in simpleGraph, I will run all tests of these functions in that module.
    #
    
    pass
