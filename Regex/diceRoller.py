import sys
import re
import random

def extractValues(s):
	regexp = re.compile(r"(?P<multiplier>[0-9]+)"
						r"d"
						r"(?P<range>([0-9]+|[fF]))")

	result = regexp.search(s)
	if result == None:
		print("didnt work")
		return 0, 0
	else:
		mul = result.group('multiplier')
		range_max = result.group('range')
	
	return int(mul), range_max
	
def rollDices(mul, range_max):
	
	print("Rolling for " + str(mul) + "d" + str(range_max))
	total = 0
	if range_max != 'F' and range_max != 'f':
		for i in range(mul):
			roll = random.randint(1, range_max)
			print("Roll: " + str(i + 1) + " = " + str(roll))
			total += roll
	else:
		for i in range(mul):
			roll = random.randint(0, 2) - 1
			print("Roll: " + str(i + 1) + " = " + str(roll))
			total += roll
			
		
	return total

	
s = ["1d6"]
if len(sys.argv) > 1:
	s = []
	for roll in sys.argv:
		if roll != sys.argv[0]:
			s.append(roll)
			
			
else:
	print("No arguments, testing 1d6")

total_rolls = 0

for roll in s:	
	multiplier, range_max = extractValues(roll)	
	if range_max != 'F' and range_max != 'f':
		print(range_max)
		range_max = int(range_max)
	roll_result = rollDices(multiplier, range_max)
	total_rolls += roll_result
	print("Total for: " + str(roll) + " = " + str(roll_result))

print("The total obtained for all rolls is: " + str(total_rolls))