#!/usr/bin/env python

'''
File:
	logger.py

Description:
	A general purpose logging module. It may be simple but it contains 
flashy colors... on Unix based systems that is! This module was wrote for
CS440 at Colorado State Universty. These colors should work through SSH,
PuTTy and on OSX's terminal as well as any Linux terminal. It's also
possible to use on Windows with some tweaks to the Windows console.

Author:
	Corey Prophitt <prophitt.corey@gmail.com> <www.marustudios.com>

License:
	GPLv3, see license.txt for more details.
'''


from datetime import datetime as dt


#
# This dictionary maps a color string to the Unix (ANSI) escape characters
# which enables the color or mode. For more information see follow the link:
#           http://en.wikipedia.org/wiki/ANSI_escape_code

ANSI_COLOR_MAP = {

	#
	# Foreground Colors
	#

	'BLACK'             : '\033[30m',       
	'RED'               : '\033[31m',        
	'GREEN'             : '\033[92m',           
	'BROWN'             : '\033[33m',            
	'BLUE'              : '\033[34m',          
	'PURPLE'            : '\033[35m',           
	'LBLUE'             : '\033[36m',           
	'GRAY'              : '\033[37m',            
	'MAGENTA'           : '\033[95m',            
	'YELLOW'            : '\033[93m',            
	'WHITE'             :         '',            

	#
	# Background Colors
	#

	'BLACKBGD'          : '\033[40m',            
	'REDBGD'            : '\033[41m',           
	'GREENBGD'          : '\033[42m',            
	'BROWNBGD'          : '\033[43m',           
	'BLUEBGD'           : '\033[44m',        
	'PURPLEBGD'         : '\033[45m',        
	'LBLUEBGD'          : '\033[46m',            
	'WHITEBGD'          : '\033[47m',            

	#
	# Special Characters and Modes
	#

	'BOLDON'            : '\033[01m',            # Turn bolding on
	'BOLDOFF'           : '\033[22m',            # Turn bolding off
	'CLEAR'             : '\033[2J',             # Clears the terminal screen
	'RESET'             : '\033[00m',            # Reset colors (default)

	}

#
#
#


class DummyColorProvidor:
	'''A dummy color providor. This providor can be used on systems where the
	ANSI codes are not available by default such as Windows.
	'''

	def disable(self):
		pass

	def is_disabled(self):
		return True

	def enable(self):
		pass

	def clear(self):
		pass

	def color(self, string, fg, bg, bold=False):
		pass
	

class UnixColorProvidor:
	'''A color providor. Uses the global color map to provide colored strings
	to the caller. This implementation is for Unix based consoles, however
	any providor can be created as long as they follow this interface.
	'''

	def __init__(self, enabled=True):
		'''Initializer, if enabled is True the ANSI color map is used.
		If enabled is False no color map is used.'''
		
		if enabled:
			self.color_map = ANSI_COLOR_MAP
		else:
			self.color_map = None

	def disable(self):
		'''Turns 'off' the color providor.'''
		
		if self.color_map:
			self.color_map = None

	def is_disabled(self):
		'''Returns True if the color providor is disabled.'''
		
		return self.color_map == None

	def enable(self):
		'''Turns 'on' the color providor.'''
		
		if self.color_map == None:
			self.color_map = ANSI_COLOR_MAP

	def clear(self):
		'''Sends the clear code to the terminal.'''

		print(self.color_map['CLEAR'])

	def color(self, string, fg, bg, bold=False):
		'''Color returns a 'colored' string. The foreground color is marked
		via the 'fg' parameter. The background color is marked via the 'bg'
		parameter. If 'bold' is True the returned text will be bold.
		'''
		
		if self.color_map:
			fg_in_map = fg in self.color_map
			bg_in_map = bg in self.color_map
			all_in_map = fg_in_map and bg_in_map
			
			if all_in_map:
				fg = self.color_map[fg]
				bg = self.color_map[bg]
				reset = self.color_map['RESET']
			else:
				bg    = ''
				fg    = ''
				reset = ''
				
			if bold == True and all_in_map:
				string = self.make_bold(string)

			return '{0}{1}{2}{3}'.format(fg, string, bg, reset)

		return string

	def make_bold(self, string):
		'''Takes a string in and returns the same string except bold.'''
		
		return self.color_map['BOLDON'] + string + self.color_map['BOLDOFF']


class DummyLogger(object):
	'''A dummy logger. You can replace a ConsoleLogger with a dummy if you
	wish to silence all output. This is useful for quiet modes or optimized
	modes where performance is beging bogged down by writing to the console.
	'''

	def enable_colors(self):
		pass

	def disable_colors(self):
		pass

	def write(self, msg, tag=''):
		pass

	def write_if(self, exp, msg, tag=''):
		pass

	def write_ife(self, exp, msg, tag, msg2, tag2):
		pass

	def debug_write(self, msg, tag='INFO'):
		pass

	def debug_write_if(self, exp, msg, tag='INFO'):
		pass

	def debug_write_ife(self, exp, msg, tag, msg2, tag2):
		pass

	def clear_screen(self):
		pass

class ConsoleLogger(object):
	'''A simple class with a number of printing functions. All output goes to
	the standard output (terminal, console, etc.).
	'''

	#
	# Static Color Setup
	#

	# Message Colors
	NOTICE              = 'WHITE'
	INFO                = 'WHITE'
	EVENT               = 'WHITE'
	WARNING             = 'WHITE'
	ERROR               = 'WHITE'

	NOTICE_BGD          = 'GRAY'
	INFO_BGD            = 'GRAY'
	EVENT_BGD           = 'GRAY'
	WARNING_BGD         = 'GRAY'
	ERROR_BGD           = 'GRAY'

	# Tag Colors
	NOTICE_TAG          = 'PURPLE'
	INFO_TAG            = 'WHITE'
	EVENT_TAG           = 'GREEN'
	WARNING_TAG         = 'YELLOW'
	ERROR_TAG           = 'RED'

	NOTICE_TAG_BGD      = 'GRAY'
	INFO_TAG_BGD        = 'GRAY'
	EVENT_TAG_BGD       = 'GRAY'
	WARNING_TAG_BGD     = 'GRAY'
	ERROR_TAG_BGD       = 'GRAY'

	# Time Colors
	TIME                = 'MAGENTA'
	TIME_BGD            = 'GRAY'

	def __init__(self, color_providor):
		'''Initializer, takes a color providor such as a UnixColorProvidor, or
		a DummyProvidor.'''

		self.color_providor = color_providor

	def enable_colors(self):
		'''Enables colored output if the providor provides it.'''

		self.color_providor.enable()

	def disable_colors(self):
		'''Disables colored output.'''

		self.color_providor.disable()
		
	def write(self, msg, tag='INFO'):
		'''Writes a log message to standard out. The tag parameter is optional.
		The default tag is 'INFO'. Other tags include, 'EVENT', 'WARNING', 
		and 'NOTICE'. The tags represent the type of message.'''

		print(self.resolve_colors(msg, tag))

	def write_if(self, exp, msg, tag='INFO'):
		'''Writes a message to standard out if the expression is True.'''

		if exp:
			self.write(msg, tag)

	def write_ife(self, exp, msg, tag, msg2, tag2):
		'''Writes a message to standard out if the expression is True. If the
		expression is false the second message is wrote.'''

		if exp:
			self.write(msg, tag)
		else:
			self.write(msg2, tag2)

	def debug_write(self, msg, tag='INFO'):
		'''Same as write, but only prints in __DEBUG__ mode.'''

		if __debug__:
			print(self.resolve_colors(msg, tag))

	def debug_write_if(self, exp, msg, tag='INFO'):
		'''Same as write, but only prints in __DEBUG__ mode.'''

		if __debug__ and exp:
			self.write(msg, tag)

	def debug_write_ife(self, exp, msg, tag, msg2, tag2):
		'''Same as write, but only prints in __DEBUG__ mode.'''

		if __debug__:
			if exp:
				self.write(msg, tag)
			else:
				self.write(msg2, tag2)

	def clear_screen(self):
		'''Clears the terminal screen if the providor is able to. If the 
		providor is unable to clear the screen then nothing happens.'''

		self.color_providor.clear()   


	def resolve_colors(self, msg, tag):
		'''Determines which colors to paint each category (tag/message).'''

		if self.color_providor.is_disabled():
			return '{0}\t{1} \t{2}'.format(str(dt.now()), tag, msg)

		time = self.color_providor.color(str(dt.now()) + '\t ',
										 self.TIME,
										 self.TIME_BGD)
		
		message = ''
		ntag = ''
		
		if tag == 'NOTICE':

			message = self.color_providor.color(' ' + msg,
												self.NOTICE,
												self.NOTICE_BGD)
			
			ntag = self.color_providor.color(' ' + tag + ' ',
											 self.NOTICE_TAG,
											 self.NOTICE_TAG_BGD)
			
		elif tag == 'INFO':
			
			message = self.color_providor.color(' ' + msg,
												self.INFO,
												self.INFO_BGD)
			
			ntag = self.color_providor.color(' ' + tag + '\t ',
											 self.INFO_TAG,
											 self.INFO_TAG_BGD)
			
		elif tag == 'EVENT':
			
			message = self.color_providor.color(' ' + msg,
												self.EVENT,
												self.EVENT_BGD)
			
			ntag = self.color_providor.color(' ' + tag + '\t ',
											 self.EVENT_TAG,
											 self.EVENT_TAG_BGD)
						
		elif tag == 'WARNING':
			
			message = self.color_providor.color(' ' + msg,
												self.WARNING,
												self.WARNING_BGD)
			
			ntag = self.color_providor.color(' ' + tag,
											 self.WARNING_TAG,
											 self.WARNING_TAG_BGD)
		   
		elif tag == 'ERROR':
			
			message = self.color_providor.color(' ' + msg,
												self.ERROR,
												self.ERROR_BGD)
			
			ntag = self.color_providor.color(' ' + tag + '\t ',
											 self.ERROR_TAG,
											 self.ERROR_TAG_BGD)
		else:  
			# This can occur if the tag was not in the map at all..
			# Uses the default tag and message that were passed into the
			# function.
			ntag = tag
			message = msg
			
		return '{0}{1}{2}'.format(time, ntag, message)

		
if __name__ == '__main__':

	import unittest


	print('Executing logger.py tests.')


	#
	# Unit Tests for the DummyColorProvidor class
	#

	class TestDummyColorProvidor(unittest.TestCase):

		def setUp(self):
			self.ansi_providor = DummyColorProvidor()
			self.console_logger = ConsoleLogger(self.ansi_providor)

		def tearDown(self):
			pass

		def test_is_dummy_disabled(self):
			self.assertTrue(self.console_logger.color_providor.is_disabled())


	#
	# Unit Tests for the UnixColorProvidor class
	#

	class TestUnixColorProvidor(unittest.TestCase):

		def setUp(self):
			pass

		def tearDown(self):
			pass

		def test_default(self):
			providor = UnixColorProvidor()
			self.assertFalse(providor.is_disabled())

		def test_false(self):
			providor = UnixColorProvidor(False)
			self.assertTrue(providor.is_disabled())

		def test_true(self):
			providor = UnixColorProvidor(True)
			self.assertFalse(providor.is_disabled())

		def test_enable(self):
			providor = UnixColorProvidor(False)
			providor.enable()
			self.assertFalse(providor.is_disabled())

		def test_disable(self):
			providor = UnixColorProvidor(True)
			providor.disable()
			self.assertTrue(providor.is_disabled())

		def test_disabled_color(self):
			providor = UnixColorProvidor()
			providor.disable()
			orig_string = "HELLO"
			string = providor.color(orig_string, 'RED', 'BLUEBGD')
			self.assertEquals(string, orig_string)

		def test_disabled_color2(self):
			providor = UnixColorProvidor(False)
			orig_string = "HELLO"
			string = providor.color(orig_string, 'RED', 'BLUEBGD')
			self.assertEquals(string, orig_string)

		def test_disabled_color3(self):
			providor = UnixColorProvidor(False)
			orig_string = "HELLO"
			string = providor.color(orig_string, 'RED', 'BLUEBGD', True)
			self.assertEquals(string, orig_string)

		def test_disabled_color4(self):
			providor = UnixColorProvidor(False)
			orig_string = "HELLO"
			string = providor.color(orig_string, '', '')
			self.assertEquals(string, orig_string)

		def test_disabled_color5(self):
			providor = UnixColorProvidor(False)
			orig_string = "HELLO"
			string = providor.color(orig_string, '', '', True)
			self.assertEquals(string, orig_string)

		def test_enabled_color(self):
			providor = UnixColorProvidor()
			orig_string = "HELLO"
			string = providor.color(orig_string, 'RED', 'BLUEBGD')
			prop_string = "\033[31mHELLO\033[44m\033[00m"
			self.assertEquals(string, prop_string)

		def test_enabled_color2(self):
			providor = UnixColorProvidor(True)
			orig_string = "HELLO"
			string = providor.color(orig_string, 'RED', 'BLUEBGD', True)
			prop_string = "\033[31m\033[01mHELLO\033[22m\033[44m\033[00m"
			self.assertEquals(string, prop_string)

		def test_enabled_color3(self):
			providor = UnixColorProvidor(True)
			orig_string = "HELLO"
			string = providor.color(orig_string, 'NYI', 'NYI')
			self.assertEquals(string, orig_string)

		def test_enabled_color4(self):
			providor = UnixColorProvidor(True)
			orig_string = "HELLO"
			string = providor.color(orig_string, 'NYI', 'NYI', True)
			self.assertEquals(string, orig_string)

		def test_enabled_color5(self):
			providor = UnixColorProvidor(True)
			orig_string = "HELLO"
			string = providor.color(orig_string, 'RED', 'NYI', True)
			self.assertEquals(string, orig_string)

		def test_enabled_color6(self):
			providor = UnixColorProvidor(True)
			orig_string = "HELLO"
			string = providor.color(orig_string, 'NYI', 'REDBG', True)
			self.assertEquals(string, orig_string)


	#
	# Note: No Unit Tests wrote for ConsoleLogger, it's implementation often
	# changes and there is no easy way to test output. However, I feel confident
	# in it due to the careful providor tests and manual testing. 
	#

		
	#
	# Execute all the Unit Tests and exit.
	#

	unittest.main()  