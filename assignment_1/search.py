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

def breadthFirstSearch(startState, endState, successorsf):
    '''
    '''

    unvisited = [startState]
    path = []

    while unvisited:
        node = unvisited.pop()
        path.append(node)
        if node == endState:
            return path

        # Let's go across and see if the endNode is here..
        children = successorsf(node)
        for childNode in children:
            if childNode == endState:
                path.append(childNode)
                return path
            if childNode not in path and childNode not in unvisited:
                unvisited.append(childNode)

    # Returns an empty list, no path was available from start to end.
    return list()
            

def depthFirstSearch(startState, endState, successorsf):
    '''
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
