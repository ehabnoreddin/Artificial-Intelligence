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
    import hw6
    import minconflicts as mc
except ImportError as ie:
    print "Error importing a required file ({}).".format(ie)
    sys.exit(-1)

###############################################################################
###############################################################################


###############################################################################
# Utilities
###############################################################################

DEBUG = False

def write(msg):
    if DEBUG:
        print msg

def dumpDict(msg, keyName, valueName, dictionary):
    if DEBUG:
        print msg
        for key in dictionary:
            print "{}:{} -> {} -> {}".format(keyName, valueName, key, dictionary[key])

def dumpTuple(msg, valueName, tuple):
    if DEBUG:
        print msg
        for value in tuple:
            print "{}: {}".format(valueName, value)

write("Debug mode is on.")

###############################################################################
###############################################################################


###############################################################################
# Solution-specific stuff!
###############################################################################

# Number of times to run part1()
PARTONERUNS = 3

# Number of times to run part2()
PARTTWORUNS = 3

# Classrooms (22 of them)
vars = hw6.Classes

# Classroom -> (Room, Time) pairs (22 of them, 24 domain values each..)
domains = dict( [(classRoom, hw6.RoomTimePairs[:]) for classRoom in vars] )

# Defines the constrains between our ClassRoom -> RoomTimePair
def constraints(var, val, var2, val2):
    '''Returns False if the constraints were not satisfied. True otherwise.'''

    # Classes can't be in the same room at the same time
    if val is val2:
        write('vals equal: {} is {}'.format(var, var2))
        return False

    # Non-100 level classes can't exist at the same time slot
    if var[2] is var2[2] and var[2] is not '1' and val[1] is val2[1]:
        return False

    return True

# The other classrooms near each class (all other classes but itself, 21 vals)
neighbors = dict( [(classRoom,
                    filter(lambda x: x != classRoom, vars))
                   for classRoom in vars] )


def part1():
    '''Completes one pass of homework 6's part 1.'''
    write("Executing part 1")
    sol, steps = mc.min_conflicts(vars, domains, constraints, neighbors)
    write(sol), write(len(sol))
    display(sol, steps)

def bonusPoints(solution):
    points = 0

    for k in solution:
        v = solution[k]
        if (k == 'CS160' or k == 'CS161') and (v[1] == '1' or v[1] == '2'):
            points += 1
        if v[1] != '9' or v[1] != '12' or v[1] != '4':
            points += 1

    return points

def part2():
    '''Completes one pass of homework 6's part 2.'''
    write("Executing part 2")

    runDict = {}
    for i in range(100):
        sol, steps = mc.min_conflicts(vars, domains, constraints, neighbors)
        points = bonusPoints(sol)
        runDict[points] = (sol, steps)

    highest = None
    for k in runDict:
        if highest == None or highest < k:
            highest = k

    print ""
    print "The solution with least violations/most preferences was found"
    display(runDict[highest][0], runDict[highest][1], highest)

def display(solution, steps, prefs = None):
    '''Display the solution in a pretty way!'''

    if not solution:
        print "No solution was found"
        return

    print "The steps used were {}".format(steps)
    if prefs != None:
        print "The preference count was {}".format(prefs)

    print ""
    print " TIME   CSB 160    CSB 325    CSB  425"
    for time in hw6.Times:
        print getTimeString(solution, time)

def getTimeString(solution, time):
    '''A helper function to generate rows in the display.'''

    c130 = "None"
    c325 = "None"
    c425 = "None"

    for classRoom in solution:
        pair = solution[classRoom]
        if pair[1] == time:
            if pair[0] == 'CSB 130':
                c130 = classRoom
            elif pair[0] == 'CSB 325':
                c325 = classRoom
            else:
                c425 = classRoom

    return "   {:2}     {:5}     {:5}       {:5}".format(time, c130, c325, c425)

###############################################################################
###############################################################################


###############################################################################
# Main
###############################################################################

def main():
    for i in range(PARTONERUNS):
        part1()
    for i in range(PARTTWORUNS):
        part2()

if __name__ == '__main__':
    main()

###############################################################################
###############################################################################