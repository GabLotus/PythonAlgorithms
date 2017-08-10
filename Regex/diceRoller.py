import sys
import re
import random

def extractValues(s):
	regexp = re.compile(r"(?P<multiplier>[0-9]+)"
						r"d"
						r"(?P<range>[0-9]+)")

	result = regexp.search(s)
	if result == None:
		print("didnt work")
		return 0, 0
	else:
		mul = result.group('multiplier')
		range_max = result.group('range')
	
	return int(mul), int(range_max)
	
def rollDices(mul, range_max):
	print("Rolling for " + str(mul) + "d" + str(range_max))
	total = 0
	for i in range(mul):
		roll = random.randint(1, range_max)
		print(roll)
		total += roll
		
	return total

	
s = "1d6"
if len(sys.argv) > 1:
	s = sys.argv[1]
else:
	print("No arguments, testing 1d6")

multiplier, range_max = extractValues(s)
	
roll = rollDices(multiplier, range_max)

print("The total obtained is: " + str(roll))