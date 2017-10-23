import sys
# Algorithm to determine if two string have only one character or less of difference.
def generalCase(s,d):
	if len(s) - len(d) > 1:
		return False

	mismatch = 0

	for i in range(len(d)):
		while s[i] != d[i]:
			mismatch += 1
			if mismatch > 1:
				return False
			if len(s) > len(d):
				s = s[0: i] + s[i+1: len(s)]
			else:
				break

	return True

s = "abacd"
d = "abcd"

if len(sys.argv) < 3:
	print("testing with default value")
else:
	s = sys.argv[1]
	d = sys.argv[2]

if len(s) < len(d):
	s, d = d, s

oneAway = generalCase(s, d)




print(oneAway)