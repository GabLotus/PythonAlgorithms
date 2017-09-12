import sys
number = 1
if len(sys.argv) > 1:
    number = sys.argv[1]

number = int(number)
print(bin(number))
print(bin(2|1))