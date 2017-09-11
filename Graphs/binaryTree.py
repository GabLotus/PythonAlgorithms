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
		

def appendByLevel(root, lists):
	queue = []
	queue.append((root, 0))
	while len(queue) > 0:
		node, level = queue.pop(0)
		print(node.data, level)
		if len(lists) <= level:
			lists.append([])
		lists[level].append(node.data)
		if node.left is not None:
			queue.append((node.left, level + 1))
		if node.right is not None:
			queue.append((node.right, level + 1))

def checkHeight(root):
	if root is None:
		return 0

	if root.left is not None:
		left_height = checkHeight(root.left)
	else:
		left_height = 0

	if root.right is not None:
		right_height = checkHeight(root.right)
	else:
		right_height = 0
	
	if left_height > right_height:
		highest = left_height
	else:
		highest = right_height
	
	return 1 + highest

def isBalanced(root):
	if root is None:
		return True

	if abs(checkHeight(root.left) - checkHeight(root.right)) < 2:
		if isBalanced(root.left) == False or isBalanced(root.right) == False:
			return False
		else:
			return True
	else:
		 return False

def isBinarySearchTree(root):
	left_good = True
	right_good = True
	if root is None:
		return True
	if root.left is not None:
		if root.left.data > root.data:
			return False
		left_good = isBinarySearchTree(root.left)
	if root.right is not None:
		if root.right.data < root.data:
			return False
		right_good = isBinarySearchTree(root.right)
	
	return left_good and right_good

	




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

root2 = Node(5)
insertNode(root2, 1)
insertNode(root2, 0)
insertNode(root2, 2)

root3 = Node(3)
insertNode(root3, 2)
insertNode(root3, 4)


root4 = Node(5)
insertNode(root4, 1)
insertNode(root4, 7)
insertNode(root4, 6)
insertNode(root4, 8)




inOrderPrint(root)
path = []
found = findNode(root, 7, path)
if found:
	print(found)
else:
	print("no node found")
	
array = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(array)
array_a, array_b, median = pickMedian(array)
yo = None
minHeightInsertion(yo, array)
list_of_list = []
appendByLevel(root, list_of_list)
print(list_of_list)
print(checkHeight(root4))
print(isBalanced(root4))
print(isBinarySearchTree(root4))
root4.left.left = Node(10)  # root4 not a binary tree anymore
print(isBinarySearchTree(root4))