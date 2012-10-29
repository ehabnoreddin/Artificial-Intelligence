#!/usr/bin/env python -O

'''
	File: 	        schedule.py
	Author:         Corey Prophitt
	License:        GPLv3, see license.txt for more details.

    Description:
        Homework assignment 6 for CSU's CS440. 
'''

###############################################################################
# Imports
###############################################################################

import sys

try:
    import minconflicts as mc
except ImportError as ie:
    print "Error importing a required file ({}).".format(ie)
    sys.exit(-1)

###############################################################################
###############################################################################


###############################################################################
# Globals
###############################################################################

# Class Rooms: CSB 130,  CSB 325, CSB 425
# Class Times: 9, 10, 11, 12, 1, 2, 3, 4

VARIABLES = (
    'CS160', 'CS161', 'CS200', 'CS270', 'CS253', 'CS320', 'CS314', 'CS370',
    'CS410', 'CS414', 'CS420', 'CS440', 'CS430', 'CS451', 'CS453',
    'CS510', 'CS514', 'CS517', 'CS518', 'CS520', 'CS530', 'CS540'
)

roomsAndTimes = (
    ('CSB130', 9), ('CSB130', 10), ('CSB130', 11), ('CSB130', 12),
    ('CSB130', 1), ('CSB130', 2), ('CSB130', 3), ('CSB130', 4),
    ('CSB325', 9), ('CSB325', 10), ('CSB325', 11), ('CSB325', 12),
    ('CSB325', 1), ('CSB325', 2), ('CSB325', 3), ('CSB325', 4),
    ('CSB425', 9), ('CSB425', 10), ('CSB425', 11), ('CSB425', 12),
    ('CSB425', 1), ('CSB425', 2), ('CSB425', 3), ('CSB425', 4)
)

DOMAINS = dict( [ (room, roomsAndTimes) for room in VARIABLES ] )

del roomsAndTimes # we don't need this hanging around any more..

###############################################################################
###############################################################################


###############################################################################
# Functions
###############################################################################

def constraints(var, val, var2, val2):
    pass

def neighbors():
    pass

def display(schedule, steps, conflicts = -1):
    '''Prints the solution to the schedule problem in a friendly way.
    Requires the solution schedule and the number of steps as input.
    '''
    pass

def main():
    '''The main script entry point.'''

    # Run min-conflicts 3 times and displays the schedule and steps taken


    # Run min-conflicts wrapper 3 times, displays schedule as well as the
    # number of violated preferences while searching and the required steps.

    print 'Hello World!'

###############################################################################
###############################################################################


###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    main()

###############################################################################
###############################################################################