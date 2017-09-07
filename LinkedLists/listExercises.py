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
	
	def appendConstructedNode(self, node):
		n = self
		while n.next is not None:
			n = n.next
		
		n.next = node
		

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
	
def findIntersection(head1, head2):
	listDict = {}
	listDict[head1] = True
	while head1.next is not None:
		listDict[head1.next] = True
		head1 = head1.next
	
	if head2  in listDict:
		return head2
	while head2.next is not None:
		if head2.next  in listDict:
			return head2.next
		else:
			head2 = head2.next
	
	return Node("nothing found")
	
def findLoop(head):
	listDict = {}
	listDict[head] = True
	while head.next is not None:
		if head.next in listDict:
			return head.next
		else:
			listDict[head.next] = True
			head = head.next 
		
	return Node("no loop found")
	
	
		
		
list = Node(5)
list.appendNode(4)
list.appendNode(3)
list.appendNode(9)
list2 = Node(8)
list2.appendNode(7)
list2.appendNode(0)
list2.appendNode(4)



interList = Node(1)
interList.appendNode(2)
interList.appendNode(3)
interList2 = Node('a')
interList2.appendNode('b')
interList2.appendNode('c')
interList2.appendNode('d')
interList2.appendNode('e')
interList.appendConstructedNode(interList2.next.next)


loopList = Node(1)
loopList.appendNode(2)
loopList.appendNode(3)
loopList.appendNode(4)
loopList.appendNode(5)
loopList.appendNode(6)
loopList.appendConstructedNode(loopList.next.next.next)

print(generateNumber(list, 1, False))
print(generateReverseNumber(list))
print(getLength(list))


printList(interList)
intersectionFound = findIntersection(interList, interList2)
print(intersectionFound.data)

print(findLoop(list).data)
print(findLoop(loopList).data)