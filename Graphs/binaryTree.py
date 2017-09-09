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
	
