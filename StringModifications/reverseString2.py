import sys

def reverseString(s):
	for i in range(0, (len(s)//2)):
		s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
		

	return s

s = list("drawer")

if len(sys.argv) > 1:
	s = list(sys.argv[1])
else:
	print("No arguments provided for execution, running program with : " + "".join(s) + " instead")

reverseString(s)
s = "".join(s)

print(s)