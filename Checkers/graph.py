#James Simbolon
#Haverford College
#Adapted from lab 6's graph.py, and as such this is adapted from JD's work.
from Checkers.constants import *

class graph:
    def __init__(self):  # construct an empty graph ...
        self.rep = {}  # .. as an empty adjacency list represented
        # as an empty dictionary

    def __str__(self):  # for printing the contents of the graph
        return str(self.rep)

    def addNode(self, node):  # add a new node to the graph, no links yet. Mutator
        if not node in self.rep:
            self.rep[node.getName()] = []  # add this node, initially no links (i.e., an island)

    def link(self, x, y):  # link two nodes already in the graph. Mutator
        #implimentation of coords is y, then x
        if x in self.rep and y in self.rep and x != y:
            direction = ''
            cont = True
            for nodes in self.listNeighbors(x):
                if nodes[0] == y:
                    cont = False
            if cont:
                if letterValues[x[0]] > letterValues[y[0]]:
                    direction = direction + north
                if letterValues[x[0]] < letterValues[y[0]]:
                    direction = direction + south
                if x[1] > y[1]:
                    direction = direction + west
                if x[1] < y[1]:
                    direction = direction + east




                self.rep[x].append([y, direction])  # link from x to y, and ...
                self.rep[y].append([x, oppositeDirection(direction)])  # ... link from y to x (undirected graph)

    def connected(self, x, y):  # returns True iff x and y are linked. acsessor
        return (y in self.rep[x]) and (x in self.rep[y])

    def listNeighbors(self, node):  # returns all neighbors of a node. acsessor
        assert node in self.rep  # node  found in graph
        return self.rep[node]

    def listNodes(self):  # returns a list containing graph nodes. acsessor
        return list(self.rep)

