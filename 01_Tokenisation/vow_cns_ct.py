import sys

cns_ct = 0
vow_ct = 0
wd_ct = 0

for c in sys.stdin.read():
	if c in 'aeiou':
		vow_ct += 1
	elif c not in '\n':
		if c not in ' ?.!,"()@#$%^&*-+=/:;':
			cns_ct += 1
		elif c == ' ':
			wd_ct +=1
			

print('number of vowels equals', vow_ct)
print('number of consonants equals', cns_ct)
print('word count equals', wd_ct+1)
print('average syllables per word equals', vow_ct//(wd_ct+1)) # whole number division since there can't be partial syllables
