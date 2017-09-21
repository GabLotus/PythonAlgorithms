def numberBinaryLenght(number):
    i = 1
    while number // 2**i > 0:
        i += 1  
    return i

def numberOfFlips(number_a, number_b):
    lenght_a = numberBinaryLenght(number_a)
    lenght_b = numberBinaryLenght(number_b)
    if lenght_b > lenght_a:
        number_a, number_b = number_b, number_a
        lenght_a, lenght_b = lenght_b, lenght_a
    count = 0
    for x in range(0, lenght_a):
        print(bin(number_a))
        if (number_a & 1) ^ (number_b & 1) == 1:
            count += 1
        number_a = number_a >> 1
        number_b = number_b >> 1
    
    return count

print(numberOfFlips(0,1))


    
    