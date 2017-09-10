class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def insertNode(root, data):
	if data <= root.data:
		if root.left is None:
			root.left = Node(data)
		else:
			insertNode(root.left, data)
	else:
		if root.right is None:
			root.right = Node(data)
		else:
			insertNode(root.right, data)


def inOrderPrint(root):
	if root.left is not None:
		inOrderPrint(root.left)
	
	print(root.data)

	if root.right is not None:
		inOrderPrint(root.right)


def findNode(root, data, path):
	path.append(root.data)
	if data == root.data:
		return path
	elif data < root.data:
		if root.left is not None:
			return findNode(root.left , data, path)
		else:
			return False
	elif data > root.data:
		if root.right is not None:
			return findNode(root.right , data, path)
		else:
			return False

def pickMedian(array):
	if len(array) > 1:
		array1 = array[0:len(array)//2]
	else:
		array1 = []

	if len(array) > 1:
		array2 = array[len(array)//2 + 1: len(array)]
	else:
		 array2 = []

	median = array[len(array)//2]
	return array1, array2, median

def minHeightInsertion(root, array):
	array_a, array_b, median = pickMedian(array)
	root = Node(median)
	arrays = []
	arrays.append(array_a)
	arrays.append(array_b)
	print(median, array_a, array_b)
	while len(arrays) > 0:
		array_c = arrays.pop(0)
		array_a, array_b, median = pickMedian(array_c)
		print(median, array_a, array_b)
		
		insertNode(root, median)
		if len(array_a) > 0:
			arrays.append(array_a)
		if len(array_b) > 0:
			arrays.append(array_b)
		





root = Node(8)
insertNode(root, 21)
insertNode(root, 3)
insertNode(root, 432)
insertNode(root, 0)
insertNode(root, -1)
insertNode(root, 123)
insertNode(root, 99)
insertNode(root, 23)
insertNode(root, 4)
insertNode(root, 1)
insertNode(root, 2)

inOrderPrint(root)
path = []
found = findNode(root, 7, path)
if found:
	print(found)
else:
	print("no node found")
	
array = [0,1,2,3,4,5,6,7,8]

print(array)
array_a, array_b, median = pickMedian(array)
yo = None
minHeightInsertion(yo, array)
