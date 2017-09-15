array = [1,1,5,5,5,6,6,6,6,6,10,11,14,14,14,16,17]
greatest = array[0]

for x, y in zip(array, range(0,len(array))):
    if x > y:
        greatest = x
    
    if y >= greatest:
        print("comparing: " + str(x) + " and: " + str(y))
        if x == y:
            print("Same!")
    else:
        print("skipping compare")



print("_________________________________________________________________")
i = 0
while i < len(array):
    if array[i] == i:
        print("Found a match at : " + str(i) + ", " + str(array[i]))
    elif array[i] > i:
        i = array[i]
        continue
    i += 1