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
    ('CSB130', 1), ('CSB130', 2),  ('CSB130', 3),  ('CSB130', 4),
    ('CSB325', 9), ('CSB325', 10), ('CSB325', 11), ('CSB325', 12),
    ('CSB325', 1), ('CSB325', 2),  ('CSB325', 3),  ('CSB325', 4),
    ('CSB425', 9), ('CSB425', 10), ('CSB425', 11), ('CSB425', 12),
    ('CSB425', 1), ('CSB425', 2),  ('CSB425', 3),  ('CSB425', 4)
)

# The same, neighbors doesn't help guide the search at all.
DOMAINS = dict( [ (room, roomsAndTimes) for room in VARIABLES ] )
NEIGHBORS = dict( [ (room, roomsAndTimes) for room in VARIABLES ] )

del roomsAndTimes # we don't need this hanging around any more..

###############################################################################
###############################################################################


###############################################################################
# Functions
###############################################################################

def constraints(var, val, var2, val2):
    '''This function weighs the constraints between variables and their 
    values. Returns True if the constraint is satisfied, False otherwise.
    '''

    result = val != val2

    if var[2] == '1' and var2[2] == '1':
        result = result and val[0] != val2[0]
    else:
        result = result and val[0] != val2[0] and val[1] != val2[1]

    return result


def display(schedule, steps, conflicts = -1):
    '''Prints the solution to the schedule problem in a friendly way.
    Requires the solution schedule and the number of steps as input.
    '''

    csb130Classes = []
    csb325Classes = []
    csb425Classes = []

    for c in schedule:
        if schedule[c][0] == 'CSB130':
            csb130Classes.append( (c, schedule[c][1]) )
        elif schedule[c][0] == 'CSB325':
            csb325Classes.append( (c, schedule[c][1]) )
        else:
            csb425Classes.append( (c, schedule[c][1]) )

    classesAt9 = "9  %s  %s  %s" % findClasses(csb130Classes, csb325Classes, csb425Classes, 9)
    classesAt10 = "10 %s  %s  %s" % findClasses(csb130Classes, csb325Classes, csb425Classes, 10)
    classesAt11 = "11 %s  %s  %s" % findClasses(csb130Classes, csb325Classes, csb425Classes, 11)
    classesAt12 = "12 %s  %s  %s" % findClasses(csb130Classes, csb325Classes, csb425Classes, 12)
    classesAt1 = "1  %s  %s  %s" % findClasses(csb130Classes, csb325Classes, csb425Classes, 1)
    classesAt2 = "2  %s  %s  %s" % findClasses(csb130Classes, csb325Classes, csb425Classes, 2)
    classesAt3 = "3  %s  %s  %s" % findClasses(csb130Classes, csb325Classes, csb425Classes, 3)
    classesAt4 = "4  %s  %s  %s" % findClasses(csb130Classes, csb325Classes, csb425Classes, 4)

    classCount = len(csb130Classes) + len(csb325Classes) + len(csb425Classes)

    print "The schedule took {} steps to find.".format(steps)
    print "A total of {} classes were scheduled.".format(classCount)
    if conflicts > -1:
        print "The total number of conflicts were {}.".format(conflicts)
    print ""

    print "   CSB130 CSB325 CSB425"
    print "-----------------------"
    print classesAt9
    print classesAt10
    print classesAt11
    print classesAt12
    print classesAt1
    print classesAt2
    print classesAt3
    print classesAt4


def findClasses(csb130Classes, csb325Classes, csb425Classes, time):

    c130 = filter(lambda x: x[1] == time, csb130Classes)
    c325 = filter(lambda x: x[1] == time, csb325Classes)
    c425 = filter(lambda x: x[1] == time, csb425Classes)

    if not c130:
        c130 = "None "
    else:
        c130 = c130[0][0]
    if not c325:
        c325 = "None "
    else:
        c325 = c325[0][0]
    if not c425:
        c425 = "None "
    else:
        c425 = c425[0][0]

    return c130, c325, c425


def main():
    '''The main script entry point.'''

    # Run min-conflicts 3 times and displays the schedule and steps taken

    sol, steps = mc.min_conflicts(VARIABLES, DOMAINS, constraints, NEIGHBORS)

    display(sol, steps)

    # Run min-conflicts wrapper 3 times, displays schedule as well as the
    # number of violated preferences while searching and the required steps.


###############################################################################
###############################################################################


###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    main()

###############################################################################
###############################################################################