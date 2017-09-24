from iterativeBinarySearch import binarySearch
from findHead import findHead

def rotatedArraySearch(n, ar):
    pivot = findHead(ar)
    left_ar = ar[0:pivot]
    right_ar = ar[pivot:len(ar)]
    if n <= left_ar[len(left_ar) - 1] and n >= left_ar[0]:
        return binarySearch(n, left_ar)
    else:
        index = binarySearch(n, right_ar)
        if index is not None:
            return pivot + index
        else:
            return None



ar = [5,6,7,8,9,0,1,2,3,4]
print(rotatedArraySearch(10, ar))

