def binarySearch(n, ar, left, right):
    mid = (left + right) // 2
    if left < right:
        return None
    if n == ar[mid]:
        return mid
    elif n < ar[mid]:
        return binarySearch(n, ar, left, mid - 1)
    elif n > ar[mid]:
        return binarySearch(n, ar, mid + 1, right)


ar = [0,2,4,8,12,26,654,999,13049,1234567]
print(binarySearch(13048, ar, 0, len(ar)-1))