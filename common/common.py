import sys, os
import pprint

def printAnything(anything):
	text = repr(anything)
	printText(text)

def printText(text):
	sys.stdout.buffer.write((pprint.pformat(text) + '\n').encode('utf8'))