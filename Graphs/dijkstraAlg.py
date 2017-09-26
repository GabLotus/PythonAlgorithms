from weightedDirectedGraph import DirectedGraph
import math

def dijkstra(initial, final, nodes):
    weights = {}
    previous = {}
    remaining = {}
    for key in dictionary:
        weights[key] = math.inf
        previous[key] = None
        remaining[key] = math.inf
    weights[initial] = 0
    remaining[initial] = 0

    while len(remaining) > 0:
        current = min(remaining, key=remaining.get)
        print(remaining)
        print(current)
        if current == final:
            break
        for neighbor in nodes[current].neighbors:
            if weights[current] + neighbor.lenght < weights[neighbor.destination.data]:
                weights[neighbor.destination.data] = weights[current] + neighbor.lenght
                remaining[neighbor.destination.data] = weights[current] + neighbor.lenght
                previous[neighbor.destination.data] = current

        del remaining[current]

    path = []
    current = final
    path.append(current)
    while previous[current] is not None:
        path.append(previous[current])
        current = previous[current]
    
    print(path)
        






my_graph = DirectedGraph(DirectedGraph.Node("a"))

node_a = my_graph.firstNode
node_b = DirectedGraph.Node("b")
node_c = DirectedGraph.Node("c")
node_d = DirectedGraph.Node("d")
node_e = DirectedGraph.Node("e")
node_f = DirectedGraph.Node("f")
node_g = DirectedGraph.Node("g")
node_h = DirectedGraph.Node("h")
node_i = DirectedGraph.Node("i")

node_a.addRoad(5, node_b)
node_a.addRoad(3, node_c)
node_a.addRoad(2, node_e)

node_b.addRoad(2, node_d)

node_c.addRoad(1, node_b)
node_c.addRoad(1, node_d)

node_d.addRoad(1, node_a)
node_d.addRoad(2, node_g)
node_d.addRoad(1, node_h)

node_e.addRoad(1, node_a)
node_e.addRoad(4, node_h)
node_e.addRoad(7, node_i)

node_f.addRoad(3, node_b)
node_f.addRoad(1, node_g)

node_g.addRoad(3, node_c)
node_g.addRoad(2, node_i)

node_h.addRoad(2, node_c)
node_h.addRoad(2, node_f)
node_h.addRoad(2, node_g)

dictionary = { "a": node_a, "b": node_b, "c": node_c, "d": node_d, "e": node_e, "f": node_f, "g": node_g, "h": node_h, "i": node_i, }

dijkstra("a", "b", dictionary)

