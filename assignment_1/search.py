#!/usr/bin/env python

'''
	File: 	    search.py
	Author:     Corey Prophitt <prophitt.corey@gmail.com>
	Class:	    CS440
	License:    GPLv3, see license.txt for more details.
'''


#
# Standard Library Imports
#

# Let's try to maintain Python 3 portability..
from __future__ import print_function


#
# The graph search algorithms (BFS, DFS)
#

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


#
# Main (individual tests)
#

if __name__ == '__main__':

	# Used for unit testing the current module when run as main 
	from unittest import main, TestCase
	
			
	#
	# BFS Tests
	#

	class BreadthFirstSearchTests(TestCase):
	
		def setUp(self):
			pass
			
		def tearDown(self):
			pass
			
		def test_not_a_valid_node(self):
			pass
		
		
	#
	# DFS Tests
	#
	
	class DepthFirstSearchTests(TestCase):
	
		def setUp(self):
			pass
			
		def tearDown(self):
			pass
			
		def test_not_a_valid_node(self):
			pass

			
	#
	# Run all tests and exit
	#
	
	main()
