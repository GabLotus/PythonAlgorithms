
def selectionSort(ar):
	for i in range(len(ar)):
		index_smallest = i
		for j in range(i, len(ar)):
			if ar[j] < ar[index_smallest]:
				index_smallest = j
		
		ar[i], ar[index_smallest] = ar[index_smallest], ar[i]
		
	return ar
		
			
		


a = [ 0, 2, 0, 3, 6, 5, 2, 1, 1, 1, 9]
a = selectionSort(a)
print(a)
