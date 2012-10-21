#!/usr/bin/env python -O

'''
	File: 	        schedule.py
	Author:         Corey Prophitt
	License:        GPLv3, see license.txt for more details.

    Description:
        Homework assignment 6 for CSU's CS440. A number of functions taken from
    class notes provided by Chuck Anderson.

    http://www.cs.colostate.edu/~anderson/cs440/index.html/doku.php?id=notes:constraintsatisfaction3
'''

###############################################################################
# Imports
###############################################################################

import random

###############################################################################
###############################################################################


###############################################################################
# Functions
###############################################################################

def min_conflicts(vars, domains, constraints, neighbors, max_steps=1000):
    """Solve a CSP by stochastic hillclimbing on the number of conflicts."""
    # Generate a complete assignment for all vars (probably with conflicts)
    current = {};
    for var in vars:
        val = min_conflicts_value(var, current, domains, constraints, neighbors)
        current[var] = val
    # Now repeapedly choose a random conflicted variable and change it
    for i in range(max_steps):
        conflicted = conflicted_vars(current,vars,constraints,neighbors)
        if not conflicted:
            return (current,i)
        var = random.choice(conflicted)
        val = min_conflicts_value(var, current, domains, constraints, neighbors)
        current[var] = val
    return (None,None)

def min_conflicts_value(var, current, domains, constraints, neighbors):
    """Return the value that will give var the least number of conflicts.
        If there is a tie, choose at random."""
    return argmin_random_tie(domains[var],
                             lambda val: nconflicts(var, val, current, constraints, neighbors))

def conflicted_vars(current,vars,constraints,neighbors):
    "Return a list of variables in current assignment that are in conflict"
    return [var for var in vars
            if nconflicts(var, current[var], current, constraints, neighbors) > 0]

def nconflicts(var, val, assignment, constraints, neighbors):
    "Return the number of conflicts var=val has with other variables."
    def conflict(var2):
        val2 = assignment.get(var2, None)
        return val2 != None and not constraints(var, val, var2, val2)
    return len(filter(conflict, neighbors[var]))

def argmin_random_tie(seq, fn):
    """Return an element with lowest fn(seq[i]) score; break ties at random.
        Thus, for all s,f: argmin_random_tie(s, f) in argmin_list(s, f)"""
    best_score = fn(seq[0]); n = 0
    for x in seq:
        x_score = fn(x)
        if x_score < best_score:
            best, best_score = x, x_score; n = 1
        elif x_score == best_score:
            n += 1
            if random.randrange(n) == 0:
                best = x
    return best

def display():
    '''Prints the solution to the schedule problem in a friendly way.'''
    pass

def main():
    '''The main script entry point.'''
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