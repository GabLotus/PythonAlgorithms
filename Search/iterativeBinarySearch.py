def binarySearch(n, ar):
    left = 0
    right = len(ar) - 1
    index = right//2
    while left <= right:
        index = (left + right)//2
        if n < ar[index]:
            right = index - 1
        elif n > ar[index]:
            left = index + 1
        else:
            return index

    return None
    
