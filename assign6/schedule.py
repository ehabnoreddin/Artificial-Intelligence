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
    import csp
except ImportError as ie:
    print "Error importing a required file ({}).".format(ie)
    sys.exit(-1)

###############################################################################
###############################################################################


###############################################################################
# Evil Globals
###############################################################################


###############################################################################
###############################################################################


###############################################################################
# Functions
###############################################################################

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