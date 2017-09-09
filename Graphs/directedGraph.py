class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []


def hasNeighbor(node, data):
    for neighbor in node.neighbors:
        if neighbor.data == data:
            return True

    return False

def findNode(node, data, stack):
    stack[node.data] = True
    if node.data == data:
        print("Node found")
        return True
    else:
        for neighbor in node.neighbors:
            if neighbor.data not in stack:
                print("visiting node: " + str(neighbor.data))
                if findNode(neighbor, data, stack):
                    return True

    return False


firstNode = Node('a')
firstNode.neighbors.append(Node('b'))
firstNode.neighbors.append(Node('c'))
firstNode.neighbors[0].neighbors.append(firstNode.neighbors[1])
firstNode.neighbors[1].neighbors.append(Node('g'))
firstNode.neighbors[1].neighbors[0].neighbors.append(Node('h'))
firstNode.neighbors.append(Node('d'))
firstNode.neighbors.append(Node('e'))
firstNode.neighbors[3].neighbors.append(Node('x'))
firstNode.neighbors[3].neighbors[0].neighbors.append(Node('z'))

firstNode.neighbors.append(Node('f'))
stack = {}
x = findNode(firstNode, 'i', stack)
print(stack)
print(x)



