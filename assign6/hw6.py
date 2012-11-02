#!/usr/bin/env python -O

'''
	File: 	        schedule.py
	Author:         Corey Prophitt
	License:        GPLv3, see license.txt for more details.

    Description:
    Homework assignment 6 for CSU's CS440.
'''

# A set of all possible classes
Classes = (
    'CS160',
    'CS161',
    'CS200',
    'CS253',
    'CS270',
    'CS314',
    'CS320',
    'CS370',
    'CS410',
    'CS414',
    'CS420',
    'CS430',
    'CS440',
    'CS451',
    'CS453',
    'CS510',
    'CS514',
    'CS517',
    'CS518',
    'CS520',
    'CS530',
    'CS540'
)

# A set of all possible classrooms
Rooms = (
    'CSB 130',
    'CSB 325',
    'CSB 425'
)

# A set of all possible class times
Times = (
    '9',
    '10',
    '11',
    '12',
    '1',
    '2',
    '3',
    '4'
)

# A set of all (Room, Time) pairs
RoomTimePairs = []
for room in Rooms:
    for time in Times:
        RoomTimePairs.append((room, time))
RoomTimePairs = tuple(RoomTimePairs)

if __name__ == '__main__':
    pass