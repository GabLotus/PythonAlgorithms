class DirectedGraph:

    
    class Node:
        def __init__(self, data):
            self.data = data
            self.neighbors = []

        def addRoad(self, lenght, destination):
            self.neighbors.append(DirectedGraph.Road(lenght,destination))

    class Road:
        def __init__(self, lenght, destination):
            self.lenght = lenght
            self.destination = destination

    def __init__(self, node):
        self.firstNode = node

        