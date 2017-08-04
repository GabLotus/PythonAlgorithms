
def mergeSort(ar):
	print(str(ar))
	low = 0
	high = len(ar)
	if len(ar) <= 1:
		return ar
	else:
		middle = (low  + high) // 2
		ar1 = mergeSort(ar[low: middle])
		ar2 = mergeSort(ar[middle:high])
		return merge(ar1, ar2)

def merge(ar1, ar2):
	ar = []
	while(len(ar1) > 0 or len(ar2) > 0):
		if len(ar1) > 0 and len(ar2) > 0:
			if ar1[0] <= ar2[0]:
				ar.append(ar1.pop(0))
				
			else:
				ar.append(ar2.pop(0))
				
		elif(len(ar1) > 0):
				ar.extend(ar1)
				ar1 = []
				
		elif(len(ar2) > 0):
				ar.extend(ar2)
				ar2 = []
	
	return ar
	

	
ar_un = [0, 1, 3, 7, 9]
ar_deux = [3, 2, -1]
ar = mergeSort(ar_deux)
print(str(ar))