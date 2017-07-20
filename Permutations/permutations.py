s = "abbc"
b = "abbcbbacbabcababcabbcabcabbcabcabbca"
c = "abbc"
d = "abbcbbac"

def verifyMultipliers(a, b, total_p):
	if(a == b):
		return (total_p + 1)
	else:
		return total_p
		
		

primes = [ 3, 5, 7, 11 ]

multiplied_s = 1
multiplied_d = 1
total = 0

for i in range(0, len(s)):
	multiplied_s = multiplied_s * primes[ord(s[i]) - 97]
	multiplied_d = multiplied_d * primes[ord(d[i]) - 97]
	
print(multiplied_s)

total = verifyMultipliers(multiplied_d, multiplied_s, total)

for x in range(0, len(d) - len(s)):

	print(multiplied_d)
	multiplied_d = (multiplied_d * primes[ord(d[x + len(s)]) - 97])/primes[ord(d[x]) - 97]
	print(d[x + len(s)])
	total = verifyMultipliers(multiplied_d, multiplied_s, total)

	#for i in range (0,len(s)):
	#	multiplied_d = multiplied_d * primes[ord(d[x+i]) - 97]
	#	print(d[x+i])
		

print(total)
