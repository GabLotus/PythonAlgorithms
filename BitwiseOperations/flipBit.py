def longestOneSequence(number):
    longest = 0
    temp = 0
    for x in range(0, numberBinaryLenght(number)):
        if number & 1 == 1:
            temp += 1
        else:
            temp = 0
        if temp > longest:
            longest = temp
        number = number >> 1
    
    return longest


def numberBinaryLenght(number):
    i = 1
    while number // 2**i > 0:
        i += 1  
    return i


def biggestSequencePossible(number):
    longest = 0
    for x in range(0, numberBinaryLenght(number)):
        mask = 1 << x
        temp = longestOneSequence(number|mask)
        if temp > longest:
            longest = temp
    
    return longest

print("looking for the longest sequence of ones in 1011011111101011. Expects: 6")
print(longestOneSequence(0b1011011111101011))
print("_____________________________________________________________________________________________________________________")
print("looking for the longest sequence of ones in 1011011111101011 provided we can flip any one bit from 0 to 1. Expects: 9")
print(biggestSequencePossible(0b1011011111101011))
print("looking for the longest sequence of ones in 1011011011101011 provided we can flip any one bit from 0 to 1. Expects: 6")
print(biggestSequencePossible(0b1011011011101011))
print("looking for the longest sequence of ones in 1011010001101011 provided we can flip any one bit from 0 to 1. Expects: 4")
print(biggestSequencePossible(0b1011010001101011))
print("looking for the longest sequence of ones in 1000000000000001 provided we can flip any one bit from 0 to 1. Expects: 2")
print(biggestSequencePossible(0b1000000000000001))