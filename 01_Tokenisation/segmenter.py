import sys
import re

line = 'XXX'
sent = ''
while line: 
	line= sys.stdin.readline()
	line = re.sub('\. ', ' \n', line)
	sys.stdout.write(line)