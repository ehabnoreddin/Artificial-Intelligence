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
    # Our implementation of BFS and DFS
    from search import breadthFirstSearch, depthFirstSearch
except ImportError:
    exit('Problem importing search.py, is the file/folder missing?')


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

             
def successorsf(node):
    '''
    Input:
             A 'node' representing the node you are looking up.
            
    Output:
             A list of children of the given 'node'.
             
             Returns an empty list if the 'node' doesn't exist, or if the node
             has no children.

             Returns an empty list if the 'node' wasn't a string or
             if the Node was None.
    '''
    
    if node is None or not isinstance(node, str):
        return []

    if node not in successors:
        return []

    return successors[node]


if __name__ == '__main__':
    
    print('Starting assignment examples\n')
    print("Breadth-first\n")
    print("path from a to a is", breadthFirstSearch('a','a', successorsf))
    print("path from a to m is", breadthFirstSearch('a','m', successorsf))
    print("path from a to z is", breadthFirstSearch('a','z', successorsf))

    print("\nDepth-first\n")
    print("path from a to a is", depthFirstSearch('a','a', successorsf))
    print("path from a to m is", depthFirstSearch('a','m', successorsf))
    print("path from a to z is", depthFirstSearch('a','z', successorsf), '\n')
    print('Finished assignment examples\n')


    # Used for additional unit testing
    from unittest import main, TestCase

    print('Starting additional unit tests\n')
    
    
    #
    # Successorsf Tests
    #
    
    class SuccessorsfTests(TestCase):

            def setUp(self):
                pass

            def tearDown(self):
                pass

            def test_no_node_in_graph(self):
                node = 'NotInGraphAtAll' 
                successors = successorsf(node)
                expected = [] 
                self.assertEquals(successors, expected)

            def test_leaf_node(self):
                node = 'z'
                successors = successorsf(node)
                expected = []
                self.assertEquals(successors, expected)

            def test_node_in_graph(self):
                node = 'a' 
                successors = successorsf(node)
                expected = ['b', 'c', 'd']
                self.assertEquals(successors, expected)      

            def test_none_node(self):
                node = None
                successors = successorsf(node)
                expected = []
                self.assertEquals(successors, expected)

            def test_nonstring_node(self):
                node = 234234 
                successors = successorsf(node)
                expected = []
                self.assertEquals(successors, expected)


    #
    # Additional Breadth First Search Tests
    #

    class BreadthFirstSearchTests(TestCase):

        def setUp(self):
            self.basic_graph = {
                'a' : ['b', 'c'],
                'b' : ['d', 'e'],
                'c' : ['f', 'g'],
                'd' : ['h', 'i'],
                'e' : ['j', 'k'],
                'f' : ['l', 'm'],
                'g' : ['n', 'o'],
            }

        def tearDown(self):
            pass

        def successorsf1(self, node):
            if node is None or not isinstance(node, str):
                return []

            if node not in self.basic_graph:
                return []

            return self.basic_graph[node]

        def test_does_not_exist_start_state(self):
            expected = []
            actual = breadthFirstSearch('DNE', 'a', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_does_not_exist_end_state(self):
            expected = []
            actual = breadthFirstSearch('a', 'DNE', self.successorsf1)
            self.assertEquals(actual, expected)
    
        def test_does_not_exist_both_states(self):
            expected = []
            actual = breadthFirstSearch('DNE', 'DNE', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_invalid_start_type(self):
            expected = []
            actual = breadthFirstSearch(123, 'a', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_invalid_end_type(self):
            expected = []
            actual = breadthFirstSearch('a', 123, self.successorsf1)
            self.assertEquals(actual, expected)

        def test_invalid_types_both(self):
            expected = []
            actual = breadthFirstSearch(123, 456, self.successorsf1)
            self.assertEquals(actual, expected)
            
        def test_basic_path_a(self):
            expected = ['a']
            actual = breadthFirstSearch('a', 'a', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_basic_path_b(self):
            expected = ['a', 'c']
            actual = breadthFirstSearch('a', 'c', self.successorsf1)
            self.assertEquals(actual, expected)
            
        def test_basic_path_c(self):
            expected = ['a', 'c', 'f']
            actual = breadthFirstSearch('a', 'f', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_basic_path_d(self):
            expected = ['b', 'e', 'k']
            actual = breadthFirstSearch('b', 'k', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_basic_path_e(self):
            expected = ['g', 'o']
            actual = breadthFirstSearch('g', 'o', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_basic_path_f(self):
            expected = ['a', 'c', 'f', 'l']
            actual = breadthFirstSearch('a', 'l', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_class_example_a(self):
            expected = ['a']
            actual = breadthFirstSearch('a', 'a', successorsf)
            self.assertEquals(actual, expected)

        def test_class_example_b(self):
            expected = ['a', 'b', 'g', 'm']
            actual = breadthFirstSearch('a', 'm', successorsf)
            self.assertEquals(actual, expected)

        def test_class_example_c(self):
            expected = ['a', 'd', 'z']
            actual = breadthFirstSearch('a', 'z', successorsf)
            self.assertEquals(actual, expected)                

        def test_none_start(self):
            expected = []
            actual = breadthFirstSearch(None, 'z', successorsf)
            self.assertEquals(actual, expected)

        def test_none_end(self):
            expected = []
            actual = breadthFirstSearch('a', None, successorsf)
            self.assertEquals(actual, expected)

        def test_none_both(self):
            expected = []
            actual = breadthFirstSearch(None, None, successorsf)
            self.assertEquals(actual, expected)
     

    #
    # Additional Depth First Search Tests
    #

    class DepthFirstSearchTests(TestCase):

        def setUp(self):
            self.basic_graph = {
                'a' : ['b', 'c'],
                'b' : ['d', 'e'],
                'c' : ['f', 'g'],
                'd' : ['h', 'i'],
                'e' : ['j', 'k'],
                'f' : ['l', 'm'],
                'g' : ['n', 'o'],
            }

        def tearDown(self):
            pass

        def successorsf1(self, node):
            if node is None or not isinstance(node, str):
                return []

            if node not in self.basic_graph:
                return []

            return self.basic_graph[node]

        def test_does_not_exist_start_state(self):
            expected = []
            actual = depthFirstSearch('DNE', 'a', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_does_not_exist_end_state(self):
            expected = []
            actual = depthFirstSearch('a', 'DNE', self.successorsf1)
            self.assertEquals(actual, expected)
    
        def test_does_not_exist_both_states(self):
            expected = []
            actual = depthFirstSearch('DNE', 'DNE', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_invalid_start_type(self):
            expected = []
            actual = depthFirstSearch(123, 'a', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_invalid_end_type(self):
            expected = []
            actual = depthFirstSearch('a', 123, self.successorsf1)
            self.assertEquals(actual, expected)

        def test_invalid_types_both(self):
            expected = []
            actual = depthFirstSearch(123, 456, self.successorsf1)
            self.assertEquals(actual, expected)

        def test_basic_path_a(self):
            expected = ['a']
            actual = depthFirstSearch('a', 'a', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_basic_path_b(self):
            expected = ['a', 'c']
            actual = depthFirstSearch('a', 'c', self.successorsf1)
            self.assertEquals(actual, expected)
            
        def test_basic_path_c(self):
            expected = ['a', 'c', 'f']
            actual = depthFirstSearch('a', 'f', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_basic_path_d(self):
            expected = ['b', 'e', 'k']
            actual = depthFirstSearch('b', 'k', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_basic_path_e(self):
            expected = ['g', 'o']
            actual = depthFirstSearch('g', 'o', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_basic_path_f(self):
            expected = ['a', 'c', 'f', 'l']
            actual = depthFirstSearch('a', 'l', self.successorsf1)
            self.assertEquals(actual, expected)

        def test_class_example_a(self):
            expected = ['a']
            actual = depthFirstSearch('a', 'a', successorsf)
            self.assertEquals(actual, expected)

        def test_class_example_b(self):
            expected = ['a', 'b', 'g', 'm']
            actual = depthFirstSearch('a', 'm', successorsf)
            self.assertEquals(actual, expected)

        def test_class_example_c(self):
            expected = ['a', 'b', 'e', 'k', 'z']
            actual = depthFirstSearch('a', 'z', successorsf)
            self.assertEquals(actual, expected)

        def test_none_start(self):
            expected = []
            actual = depthFirstSearch(None, 'z', successorsf)
            self.assertEquals(actual, expected)

        def test_none_end(self):
            expected = []
            actual = depthFirstSearch('a', None, successorsf)
            self.assertEquals(actual, expected)

        def test_none_both(self):
            expected = []
            actual = depthFirstSearch(None, None, successorsf)
            self.assertEquals(actual, expected)


    #
    # Run all tests and exit
    #
    
    main()
