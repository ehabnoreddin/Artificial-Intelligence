#!/usr/bin/env python

'''
	File: 	    simpleGraph.py
	Author:     Corey Prophitt <prophitt.corey@gmail.com>
	Class:	    CS440
	License:    GPLv3, see license.txt for more details.
'''


#
# Standard Library Imports
#

# Let's try to maintain Python 3 portability..
from __future__ import print_function

from os import name as os_name

from sys import exit


#
# Custom Library Imports
#
try:
    # My own custom logging utility
    from logger import (DummyColorProvidor, UnixColorProvidor, ConsoleLogger)
except ImportError:
    exit('Problem importing logger.py, is the file/folder missing?')

try:
    # My own debugging utilities
    from debug import debug
except ImportError:
    exit('Problem importing debug.py, is the file/folder missing?')

try:
    # Our implementation of BFS and DFS
    from search import breadthFirstSearch, depthFirstSearch
except ImportError:
    exit('Problem importing search.py, is the file/folder missing?')


#
# Setup Logging
#
if os_name is 'posix':
    color_providor = UnixColorProvidor()
else:
    # No colors on Windows yet, sorry!
    color_providor = DummyColorProvidor()

log = ConsoleLogger(color_providor)


#
# The example graph
#

# This is the example graph given for this assignment
successors = {'a':  ['b', 'c', 'd'],
              'b':  ['e', 'f', 'g'],
              'c':  ['a', 'h', 'i'],
              'd':  ['j', 'z'],
              'e':  ['k', 'l'],
              'g':  ['m'],
              'k':  ['z']}

             
def successorsf(graph, node):
    '''
    Input:
             A 'graph' represented as a Python dictionary of
             node -> children pairs.
            
             A 'node' representing the node you are looking up.
            
    Output:
             A list of children of the given 'node'.
             
             Returns an empty list if the 'node' doesn't exist, or if the node
             has no children.

             Returns None if the graph is None or if the argument wasn't a
             Python dictionary.
    '''
    
    if graph is None or not isinstance(graph, dict):
        return None

    if node not in graph:
        return list()

    return graph[node]


if __name__ == '__main__':
    
    log.write('Starting assignment examples\n')
    print("Breadth-first\n")
    print("path from a to a is", breadthFirstSearch('a','a', successorsf))
    print("path from a to m is", breadthFirstSearch('a','m', successorsf))
    print("path from a to z is", breadthFirstSearch('a','z', successorsf))

    print("\nDepth-first\n")
    print("path from a to a is", depthFirstSearch('a','a', successorsf))
    print("path from a to m is", depthFirstSearch('a','m', successorsf))
    print("path from a to z is", depthFirstSearch('a','z', successorsf), '\n')
    log.write('Finished assignment examples\n')


    # Used for additional unit testing
    from unittest import main, TestCase

    log.write('Starting additional unit tests\n', 'EVENT')
    
    
    #
    # Successorsf Tests
    #
    
    class SuccessorsfTests(TestCase):

            def setUp(self):

                    # The graph.. Node -> Accessible Node(s)
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
                    expected = [] 
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

            def test_nondictionary_graph(self):
                    node = 'a' 
                    successors = successorsf("'a' : 123", node)
                    expected = None
                    self.assertEquals(successors, expected)


    #
    # Additional Breadth First Search Tests
    #

    class BreadthFirstSearchTests(TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_path1(self):
            pass


    #
    # Additional Depth First Search Tests
    #

    class DepthFirstSearchTests(TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_path1(self):
            pass


    #
    # Run all tests and exit
    #
    
    main()
