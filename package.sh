#!/usr/bin/bash

#
# File: 	package.sh
# Author:	Corey Prophitt <prophitt.corey@gmail.com>
# Class:	CS440 @ Colorado State University
#

#
# This is a script used to package my assignment files for submission.
#

NUM=$($1)
PATH="assignment_" + $NUM
 
cd $PATH
tar cvf ..assign$NUM.tar *.py README

#
# --End--
#