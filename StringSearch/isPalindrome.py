import sys

def isPalindrome(s):
	d = {}
	s_odd = len(s)%2
	oddCounter = 0
	evenCounter = 0
	for c in s:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1
	
	for c in s:
		if c in d:
			if d[c]%2 > 0:
				oddCounter += 1
			else:
				evenCounter += 1
			del d[c]
		else:
			continue
	if oddCounter > s_odd:
		print(oddCounter)
		print(s_odd)
		return False
	else:
		return True


s = "aabcbaa"

if len(sys.argv) > 1:
	s = sys.argv[1]
else:
	print("Insuficient arguments, testing algorithm with string: " + s)

print(isPalindrome(s))

