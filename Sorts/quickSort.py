def quickSort(ar):
	
	if len(ar) <= 1:
		return ar
	
	else:
		pivot = len(ar)//2
		
		i = 0
		j = len(ar) -1
		pivot_value = ar[pivot]
		
		while i <= j:
			while ar[i] < ar[pivot]:
				i += 1
				print(i)
				
			while ar[j] > ar[pivot]:
				j -= 1
			
			if i <= j:
		
				
				ar[i], ar[j] = ar[j], ar[i]
				if i == pivot or j == pivot:
					if i == pivot:
						pivot = j
					elif j == pivot:
						pivot = i
					
					
				i += 1
				j -= 1
				
				
				

		
			
		print(str(ar[0:pivot]) + " et " + str(ar[pivot:len(ar)]))
		return quickSort(ar[0:pivot]) + quickSort(ar[pivot:len(ar)])
		

arr = [1,4,12,36,9,6,0,0,1338,-1,-9001,144]
arr = quickSort(arr)
print(str(arr))