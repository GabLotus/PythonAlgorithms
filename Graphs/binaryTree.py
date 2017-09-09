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


root = Node(8)
insertNode(root, 21)
insertNode(root, 3)
insertNode(root, 432)
insertNode(root, 0)
insertNode(root, -1)

inOrderPrint(root)
	
