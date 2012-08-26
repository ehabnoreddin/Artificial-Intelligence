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
    visited = []

    while unvisited:
        node = unvisited.pop()
        visited.append(node)
        children = successorsf(node)
        for childNode in children:
            if childNode not in visited and childNode not in unvisited:
                unvisited.append(childNode)
            if childNode == endState:
                return visited
        visited = []


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
