def recursiveMultiply(x, y):
    if y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + recursiveMultiply(x, y - 1)



print(recursiveMultiply(5,5))