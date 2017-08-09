import sys

def compressString(s):
	character_compare = s[0]
	counter = 0
	new_string = []
	
	for c in s:
		if c == character_compare:
			counter += 1
		else:
			new_string.append(str(character_compare) + str(counter))
			counter = 1
			character_compare = c
	
	new_string.append(str(character_compare) + str(counter))
	new_string = "".join(new_string)
	
	if len(s) <= len(new_string):
		return s
	else:
		return new_string
	

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaabbccccccddddddccccaaa"

if len(sys.argv) < 2:
	print("Runing algorithm with default value")
else: 
	s = sys.argv[1]

s = compressString(s)
print(s)