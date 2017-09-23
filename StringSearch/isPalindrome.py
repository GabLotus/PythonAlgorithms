import sys

def isPalindrome(s):
    for i in range(0,len(s)//2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True





s = "aaabbcbbaaa"

if len(sys.argv) > 1:
	s = sys.argv[1]
else:
	print("Insuficient arguments, testing algorithm with string: " + s)

print(isPalindrome(s))