import sys
import re

line = 'XXX'
while line:
	line = sys.stdin.readline()
	line = re.sub(' ', '\n', line)
	line.replace(',',' ,')
	line.replace(':',' :')
	line.replace('(', '( ')
	line.replace(')', ' )')
	sys.stdout.write(line)