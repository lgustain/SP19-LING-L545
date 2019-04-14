import sys

line_ct = 0
token_ct = 0
char_ct = 0

for c in sys.stdin.read():
	if c == '\n':
		line_ct += 1
	if c == ' ':
		token_ct += 1
	char_ct +=1


print(line_ct + 1)    # includes the current line
print(token_ct + 1)   # includes the current token
print(char_ct)