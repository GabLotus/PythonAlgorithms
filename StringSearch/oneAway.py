import sys

def equalLenght(s, d):
	mismatch = 0
	for c1, c2 in zip(s, d):
		if c1 != c2:
			mismatch += 1
	
	return mismatch <= 1
	

def oneLenght(s, d):
	
	fails = 0
	for i in range(len(d)):
		while i + fails >= len(s):
			if s[i + fails] != d[i]:
				while s[i+fails] != d[i]:
					fails += 1
					if fails > 1: break
				
		if fails > 1: break
	
	return fails <= 1
	
	


def moreLenght():
	return False



s = "abcd"
d = "abce"

if len(s) < len(d):
	s, d = d, s
	
oneAway = True

if len(s) == len(d):
	oneAway = equalLenght(s, d)
elif len(s) - len(d) == 1:
	oneAway = oneLenght(s, d)
else:
	oneAway = moreLenght();
	
	

print(oneAway)