# https://www.youtube.com/watch?v=SLauY6PpjW4&t=213s

def quickSort(ar, left, right):
	index = partition(ar, left, right)
	if left < index - 1:
		quickSort(ar, left, index -1)
	if right > index:
		quickSort(ar, index, right)

def partition(ar, left, right):
		pivot = ar[(left + right)//2]
		while(left <= right):
			while(arr[left] < pivot):
				left += 1
			while(arr[right] > pivot):
				right -= 1
			
			if left <= right:
				ar[left], ar[right] = ar[right], ar[left]
				left += 1
				right -= 1	
		return left

arr = [1,4,12,36,9,6,0,0,1338,-1,-9001,144]
quickSort(arr, 0, len(arr) - 1)
print(str(arr))