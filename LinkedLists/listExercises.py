class Node:
	
	def __init__(self, data):
		self.data = data
		self.next = None
	
	def appendNode(self, d):
		end = Node(d)
		n = self
		while n.next is not None:
			n = n.next
		
		n.next = end
		

def printList(head):
	print(head.data)
	if head.next is not None:
		printList(head.next)
		
def generateNumber(head, mul, reverse):
	
	if head.next is not None:
		if reverse:
			return mul * head.data + generateNumber(head.next, mul / 10, True)
		else:
			return mul * head.data + generateNumber(head.next, mul * 10, False)
	else:
		return mul * head.data

def getLength(head):
	current = head
	length = 1
	while current.next is not None:
		length += 1
		current = current.next
		
	return length
	
def generateReverseNumber(head):
	length = getLength(head)
	mul = 10 ** (length - 1)
	return generateNumber(head, mul, True)
	
	
		
		
list = Node(5)
list.appendNode(4)
list.appendNode(3)
list.appendNode(9)
list2 = Node(8)
list2.appendNode(7)
list2.appendNode(0)
list2.appendNode(4)
printList(list)

print(generateNumber(list, 1, False))
print(generateReverseNumber(list))
print(getLength(list))
