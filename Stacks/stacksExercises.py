class StackNode:
		def __init__(self, data):
			self.data = data
			self.next = None


class Stack:
	def __init__(self, top_data):
		self.top = StackNode(top_data)

	def pushData(self, data):
		new_node = StackNode(data)
		new_node.next = self.top
		self.top = new_node

	def pushNode(self, new_node):
		new_node.next = self.top
		self.top = new_node

	def popData(self):
		data = self.top.data
		self.top = self.top.next



def printList(head):
	print(head.data)
	if head.next is not None:
		printList(head.next)


my_stack = Stack(1)
my_stack.pushData(2)
my_stack.pushData(3)
my_stack.pushData(4)

printList(my_stack.top)
my_stack.popData()
printList(my_stack.top)
