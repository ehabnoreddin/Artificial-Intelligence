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
    from pyutils.logger import (DummyColorProvidor, 
                                UnixColorProvidor, 
                                ConsoleLogger)
except ImportError:
    exit('Problem importing logger.py, is the file/folder missing?')

try:
    # My own debugging utilities
    from ..pyutils.debug import debug
except ImportError:
    exit('Problem importing debug.py, is the file/folder missing?')

try:
    from search import bfs, dfs
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
# The Graph
#

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

             Returns None if the graph is None.
    '''
	if graph is None:
		return None

	if node not in graph:
		return list()

	return graph[node]


if __name__ == '__main__':
    
    log.write('Starting assignment example..')
    
    log.write('Finished assignment example.')

    print('\n\n')


    # Used for unit testing the current module when run as main 
    from unittest import main, TestCase
    
    
    #
    # Successorsf Tests
    #
    
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

    #
    # Run all tests and exit
    #
    
    main()
