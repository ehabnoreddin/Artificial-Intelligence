#!/usr/bin/env python -O

'''
	File: 	        tests.py
	Author:         Corey Prophitt <prophitt.corey@gmail.com>
	Class:	        CS440, Colorado State University.
	License:        GPLv3, see license.txt for more details.

        Description:
        
            A collection of unit tests for this assignment.
'''

###############################################################################
# Standard module import statements
###############################################################################

from __future__ import print_function       # Let's keep Python 3 in mind
from sys import exit                        # For bad import statements
from unittest import main, TestCase         # For unit testing

###############################################################################
# Custom module import statements
###############################################################################

try:
    from assign4 import opponent, opponentRandom
except ImportError as ie:
    exit("Error while importing a required module ({}).".format(ie))

###############################################################################
###############################################################################

class OpponentRandomTests(TestCase):

    def setUp(self):
        self.board = ['x', 'o', ' ']

    def tearDown(self):
        pass

    def test_valid_non_existant(self):
        expectedIndex = -1
        actualIndex = opponentRandom([])
        self.assertEquals(expectedIndex, actualIndex)
        
    def test_valid_non_existant(self):
        expectedIndex = -1
        actualIndex = opponentRandom(['x', 'y'])
        self.assertEquals(expectedIndex, actualIndex)

    def test_valid_one(self):
        expectedIndex = 2
        actualIndex = opponentRandom(self.board)
        self.assertEquals(expectedIndex, actualIndex)
        
class OpponentTests(TestCase):

    def setUp(self):
        self.board = ['x', 'o', ' ', ' ', ' ', 'x', 'o', ' ', 'x']

    def tearDown(self):
        pass

    def test_first_index(self):
        expectedIndex = 2
        actualIndex = opponent(self.board)
        self.assertEquals(expectedIndex, actualIndex)

    def test_no_index(self):
        expectedIndex = -1
        actualIndex = opponent(['x'])
        self.assertEquals(expectedIndex, actualIndex)

    def test_zero_index(self):
        expectedIndex = 0
        actualIndex = opponent([' ', 'x', 'y'])
        self.assertEquals(expectedIndex, actualIndex)

    def test_last_index(self):
        expectedIndex = 2
        actualIndex = opponent(['x', 'y', ' '])
        self.assertEquals(expectedIndex, actualIndex)

    def test_empty_list(self):
        expectedIndex = -1
        actualIndex = opponent([])
        self.assertEquals(expectedIndex, actualIndex)


if __name__ == '__main__':
    main()