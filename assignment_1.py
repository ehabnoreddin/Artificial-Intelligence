#!/usr/bin/env python

'''
	File: 	assignment_1.py
	Author: Corey Prophitt <prophitt.corey@gmail.com>
	Class:	CS440
'''

#
# Standard Library Imports
#

# Let's try to maintain Python 3 portability..
from __future__ import print_function

import os

from sys import exit

# Used for unit testing the current module when run as main 
from unittest import main, TestCase

#
# Custom Library Imports
#

try:
    # My own custom logging utility
    from pyutils.logger import (DummyColorProvidor, 
                                UnixColorProvidor, 
                                ConsoleLogger)
except ImportError:
    exit("Problem importing logger.py, is the file/folder missing?")


#
# Setup Logging
#

if os.name is 'posix':
    color_providor = UnixColorProvidor()
else:
    # No colors on Windows yet, sorry!
    color_providor = DummyColorProvidor()

log = ConsoleLogger(color_providor)


#
# The Graph(s)
#

             
def successorsf(graph, node):

    log.debug_write('Entering successorsf.')
    
    if graph is None:
        log.write('Graph is None. Returning None.', 'ERROR')
        return None

    if node not in graph:
        log.debug_write('Node not found, returning empty list.', 'EVENT')
        return list()

    log.debug_write('Node found, returning its children.', 'EVENT')
    return graph[node]


def bfs(graph, start_node, end_node):
    visited = []
    unvisited = list(start_node)
    while unvisited:
        node = unvisited.pop(0)
        transitions = successorsf(graph, node)
        if node == end_node:
            visited.append(node)
            return visited
        elif end_node in transitions:
            visited.append(node)
            visited.append(end_node)
            return visited
        elif node not in visited:
            visited.extend(list(node))
            if transitions is not None:
                unvisited.extend(transitions)
    return visited


if __name__ == '__main__':

    log.write('Starting Unit Tests..', 'NOTICE')

    class SuccessorsfTests(TestCase):

        def setUp(self):

            # The graph.. Node -> Accessible Node
            self.graph = {'a':  ['b', 'c', 'd'],
                          'b':  ['e', 'f', 'g'],
                          'c':  ['a', 'h', 'i'],
                          'd':  ['j', 'z'],
                          'e':  ['k', 'l'],
                          'g':  ['m'],
                          'k':  ['z']}

        def tearDown(self):
            pass

        def test_no_node_in_graph(self):
            node = 'z' 
            successors = successorsf(self.graph, node)
            expected = [] # Empty list when node doesn't exist!
            self.assertEquals(successors, expected)      

        def test_node_in_graph(self):
            node = 'a' 
            successors = successorsf(self.graph, node)
            expected = ['b', 'c', 'd']
            self.assertEquals(successors, expected)      

        def test_null_graph(self):
            node = 'a' 
            successors = successorsf(None, node)
            expected = None
            self.assertEquals(successors, expected)      


    # Run all the tests
    main()    
