import sys

def verifyMultipliers(a, b, total_p):
	if(a == b):
		return (total_p + 1)
	else:
		return total_p
		

print(sys.argv[0])		

if len(sys.argv) >= 3:
	s = sys.argv[1]
	d = sys.argv[2]
	print( "looking for permutations of: " + s + " in: " + d)
else:
	s = "abbc"
	d = "abbcbbac"
	print("insuficient arguments. Running the program with inputs: " + s + " and: " + d)
	
if (not (s.isalpha())) or (not (d.isalpha())):
	print("arguments must contain letters only")
	sys.exit()
	
if len(s) > len(d):
	print("first argument must be shorter or equal to the second")
	sys.exit()

s = s.lower()
d = d.lower()	

primes = [ 3,5,7,11,13,17,
		   19,23,29,31,37,
		   41,43,47,53,59,
		   61,67,71,73,79,
		   83,89,97,101,103,
		   107,109,113,127,131,
		   137,139,149,151,157,
		   163,167,173,179,181,
		   191,193,197,199 ]

multiplied_s = 1
multiplied_d = 1
total = 0

for i in range(0, len(s)):
	multiplied_s = multiplied_s * primes[ord(s[i]) - 97]
	multiplied_d = multiplied_d * primes[ord(d[i]) - 97]
	

total = verifyMultipliers(multiplied_d, multiplied_s, total)

for x in range(0, len(d) - len(s)):

	multiplied_d = (multiplied_d * primes[ord(d[x + len(s)]) - 97])/primes[ord(d[x]) - 97]
	total = verifyMultipliers(multiplied_d, multiplied_s, total)

	#for i in range (0,len(s)):
	#	multiplied_d = multiplied_d * primes[ord(d[x+i]) - 97]
	#	print(d[x+i])
		

print(total)
