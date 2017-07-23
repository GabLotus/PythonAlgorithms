

def insertCharacters(s, c):
	strings = []
	
	for x in range(0, len(s) +  1):
		sc_permutation = s[0:x] + c + s[x:len(s)]
		strings.append(sc_permutation)
		
	return strings
		


s = "abc"

new_s = insertCharacters(s[0:(len(s) - 1)], s[(len(s) - 1)])
print(new_s)