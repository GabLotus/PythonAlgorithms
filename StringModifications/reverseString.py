import sys

def reverseString(s):
	if len(s) <= 1:
		return s
	else:
		return s[len(s) - 1] + reverseString(s[0:len(s) - 1])


s = "stressed"

if len(sys.argv) > 1:
	s = sys.argv[1]
else:
	print("No arguments provided for execution, running program with : " + s + " instead")

s_reversed = reverseString(s)
print(s_reversed)