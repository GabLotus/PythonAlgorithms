
def bubbleSort(ar):
	for i in range(len(ar)):
		for j in range(0, len(ar) - i - 1):
			if ar[j] > ar[j+1]:
				ar[j], ar[j+1] = ar[j+1], ar[j]
	return ar

	
a = [ 9, 2, 0, 3, 6, 5, 2, 1, 1, 1, 0]
a = bubbleSort(a)
print(a)