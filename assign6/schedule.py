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

DEBUG = True

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
PARTONERUNS = 1

# Number of times to run part2()
PARTTWORUNS = 0

# Classrooms
vars = hw6.Classes
write("Variable count = {}".format(len(vars)))
dumpTuple("The Variables", "ClassRoom", vars)

# Classroom -> (Room, Time) pairs
domains = dict( [(classRoom, hw6.RoomTimePairs) for classRoom in vars] )
write("Domain count = {}".format(len(domains)))
write("Domain length = {}".format(len(domains['CS160'])))
dumpDict("The Domains", "ClassRoom", "RoomTimePair", domains)

# Defines the constrains between our ClassRoom -> RoomTimePair
def constraints(var, val, var2, val2):
    '''Returns False if the constraints were not satisfied. True otherwise.'''

    write("Var: {}, Val: {}\nVar2: {}, Val2: {}".format(var, val, var2, val2))

    return True

# The other classrooms near each class (all other classes)
neighbors = dict( [(classRoom, vars) for classRoom in vars] )
write("Neighbor count = {}".format(len(neighbors)))
write("Neighbor length = {}".format(len(neighbors['CS160'])))
dumpDict("The Neighbors", "ClassRoom", "Neighbors", neighbors)

def part1():
    '''Completes one pass of homework 6's part 1.'''
    write("Executing part 1")
    sol, steps = mc.min_conflicts(vars, domains, constraints, neighbors)
    write(sol)
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
    for i in range(10):
        sol, steps = mc.min_conflicts(vars, domains, constraints, neighbors)
        points = bonusPoints(sol)
        runDict[points] = (sol, steps)

    highest = None
    for k in runDict:
        if highest == None or highest < k:
            highest = k

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

    c160 = "None"
    c325 = "None"
    c425 = "None"

    for classRoom in solution:
        pair = solution[classRoom]
        if pair[1] == time:
            if pair[0] == 'CSB 160':
                c160 = classRoom
            elif pair[0] == 'CSB 325':
                c325 = classRoom
            else:
                c425 = classRoom

    return "   {:2}     {:5}     {:5}       {:5}".format(time, c160, c325, c425)

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