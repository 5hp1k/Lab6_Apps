from Vertex import Vertex
from collections import deque


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def person_is_seller(vertex):
    return vertex.getId()[0] == 'a'

def search(graph, name):
    search_queue = deque()
    search_queue += graph.getVertex(name).getConnections()
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person.getId() + " is a mango seller!")
                return True
            else:
                search_queue += graph.getVertex(person).getConnections()
                searched.add(person)
    return False