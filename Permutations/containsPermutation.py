import sys

	

print(sys.argv[0])		

if len(sys.argv) >= 3:
	s = sys.argv[1]
	d = sys.argv[2]
	print( "Searching for the elements required to permute: " + s + " in: " + d)
else:
	s = "abbc"
	d = "abbcbbac"
	print("insuficient arguments. Running the program with inputs: " + s + " and: " + d)
	
if (not (s.isalpha())) or (not (d.isalpha())):
	print("arguments must contain letters only")
	sys.exit()
	
if len(s) > len(d):
	print(False)
	sys.exit()
	
s_table = {}
d_table = {}
permutationPresent = True
	
for c in s:
	if c in s_table:
		s_table[c] += 1
	else:
		s_table[c] = 1

for c in d:
	if c in d_table:
		d_table[c] += 1
	else:
		d_table[c] = 1

for c in s:
	if c not in d_table:
		permutationPresent = False
	if c in d_table:
		if s_table[c] > d_table[c]:
			permutationPresent = False

print(permutationPresent)
	