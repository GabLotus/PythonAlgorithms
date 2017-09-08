class StackNode:
		def __init__(self, data):
			self.data = data
			self.next = None


class Stack:
	def __init__(self, top_data):
		if top_data is not None:
			self.top = StackNode(top_data)
		else:
			self.top = None

	def pushData(self, data):
		new_node = StackNode(data)
		new_node.next = self.top
		self.top = new_node

	def pushNode(self, new_node):
		if self.isEmpty():
			self.top = new_node
			self.top.next = None
		else:
			new_node.next = self.top
			self.top = new_node

	def popData(self):
		data = self.top.data
		self.top = self.top.next
		return data

	def popNode(self):
		node_to_return = self.top
		self.top = self.top.next
		return node_to_return

	def peekData(self):
		return self.top.data

	def isEmpty(self):
		return self.top is None



def printList(head):
	print(head.data)
	if head.next is not None:
		printList(head.next)

def findMin(stack):
	min = stack.peekData()
	current = stack.top
	while current.next is not None:
		if current.next.data < min:
			min = current.next.data
		current = current.next
	return min

def sortStack(unsorted_stack):
	buffer = Stack(None)
	sorted_stack = Stack(None)
	while unsorted_stack.isEmpty() == False:
		min = findMin(unsorted_stack)
		current = unsorted_stack.top.data
		while current > min:
			buffer.pushNode(unsorted_stack.popNode())
			current = unsorted_stack.top.data

		sorted_stack.pushNode(unsorted_stack.popNode())
		while buffer.isEmpty() == False:
			unsorted_stack.pushNode(buffer.popNode())

	return sorted_stack
		

		


	

	


my_stack = Stack(1)
my_stack.pushData(2)
my_stack.pushData(3)
my_stack.pushData(8)
my_stack.pushData(4)
my_stack.pushData(98)
my_stack.pushData(-4)
my_stack.pushData(8)
my_stack.pushData(0)

#print(findMin(my_stack))
my_stack = sortStack(my_stack)
printList(my_stack.top)

