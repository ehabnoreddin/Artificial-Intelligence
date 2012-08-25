#!/usr/bin/env python

'''
    File:
        debug.py

    Description:
        A few debug utility functions wrote while working on CS440 problems.
    
    Author:
        Corey Prophitt <prophitt.corey@gmail.com> <www.marustudios.com>

    License:
        GPLv3, see license.txt for more details.
'''


if __debug__:
	from pdb import set_trace

	
def debug():
	'''Wraps pdb's set_trace() to only work in debug mode. If the current mode is
	not debug then the code will be optimized out.'''
	
	if __debug__:
		set_trace()

		
if __name__ == '__main__':
	pass