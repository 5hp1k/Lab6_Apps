from Graph import Graph


def deixtra(graph, start, end):
    distances = {vid: float('inf') if vid != start else 0 for vid in graph.getVertices()}
    previous_vertices = {vid: None for vid in graph.getVertices()}
    visited = set()

    while distances:
        current = graph.getVertex(min(distances, key=distances.get))
        cid = current.getId()
        visited.add(cid)

        if cid == end:
            break

        neighbors = current.getConnections()
        for neighbor in neighbors:
          nid = neighbor.getId()
          if neighbor not in visited:
              weight = current.getWeight(neighbor)
              distance = distances[cid] + weight
              if nid in distances and distance < distances[nid]:
                  distances[nid] = distance
                  previous_vertices[nid] = current

        del distances[cid]

    if previous_vertices[end]:
        path = []
        current = graph.getVertex(end)
        while current:
            path.insert(0, current.getId())
            current = previous_vertices[current.getId()]
        return path, distances[end]
    else:
        return None, None


def getCities(graph):
    start = input('Enter starting city: ')
    end = input('Enter end city: ')
    if start not in graph or end not in graph:
        raise ValueError('Wrong city name!')
    return start, end


g = Graph()

g.addEdge('Мариинск', 'Яя', 106)
g.addEdge('Мариинск', 'Яшкино', 240)
g.addEdge('Мариинск', 'Юрга', 264)
g.addEdge('Мариинск', 'Анжеро-Судженск', 135)
g.addEdge('Яя', 'Кемерово', 173)
g.addEdge('Яшкино', 'Яя', 118)
g.addEdge('Яшкино', 'Томск', 152)
g.addEdge('Юрга', 'Яшкино', 47)
g.addEdge('Юрга', 'Томск', 112)
g.addEdge('Юрга', 'Анжеро-Судженск', 136)
g.addEdge('Томск', 'Кемерово', 217)


def main():
    start, end = getCities(g)
    path, distance = deixtra(g, start, end)
    if path is None and distance is None:
        print('The path between these cities does not exist')
    print(f'Path: {path}, distance: {distance}')
