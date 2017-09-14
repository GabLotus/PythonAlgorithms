number = 1234

i = 0
while 10 ** i < number:
    i += 1

lenght = i
new_number = 0
for x in range(0, lenght):
    new_number += (number % (10 ** (x + 1))//(10 ** x)) * (10 ** (lenght - x - 1))

print(new_number)