from graph import Graph, Edge, Vertex

def visit_mate(graph: Graph, visited: set, antecessors: dict, vertices_X: list, vertices_Y: list, vertex: Vertex):
    visited.add(vertex)
    neighbors = graph.get_neighbors_positive_not_oriented(vertex)
    for neighbor in neighbors:
        if neighbor not in visited:
            visited.add(neighbor)
            antecessors[neighbor] = vertex
            if vertex in vertices_X:
                vertices_Y.append(neighbor)
            elif vertex in vertices_Y:
                vertices_X.append(neighbor)
            else:
                raise Exception("Vertex not found in not in vertices_X neither in vertices_Y.")
            visit_mate(graph, visited, antecessors, vertices_X, vertices_Y, neighbor)
                
def separate_mates(graph: Graph):
    visited = set()
    antecessors = dict()
    for vertex in graph.vertices:
        antecessors[vertex] = None

    vertices_X = list()
    vertices_Y = list()

    i = 0
    while len(visited) < len(graph.vertices):
        vertex = graph.vertices[i]
        if vertex not in visited:
            vertices_X.append(vertex)
            visit_mate(graph, visited, antecessors, vertices_X, vertices_Y, vertex)
        i += 1
        if i >= len(graph.vertices):
            raise Exception("Not all vertices were separated!")
    
    return vertices_X, vertices_Y

def depth_first_hopcroft_karp(graph: Graph, distance: dict, mate: dict, vertex: Vertex | None) -> None:
    if vertex is not None:
        neighbors = graph.get_neighbors_positive(vertex)
        for neighbor in neighbors:
            if distance[mate[neighbor]] == distance[vertex] + 1:
                if depth_first_hopcroft_karp(graph, distance, mate, mate[neighbor]):
                    mate[neighbor] = vertex
                    mate[vertex] = neighbor

                    return True
        
        distance[vertex] = float('inf')
        return False
    
    return True

def breadth_first_hopcroft_karp(graph: Graph, vertices_X: list[Vertex], vertices_Y: list[Vertex], distance: dict, mate: dict) -> None:
    queue = list()

    for vertex in vertices_X:
        if mate[vertex] == None:
            distance[vertex] = 0
            queue.append(vertex)
        else:
            distance[vertex] = float('inf')
    
    distance[None] = float('inf')

    while len(queue) > 0:
        vertex = queue.pop(0)
        if distance[vertex] < distance[None]:
            neighbors = graph.get_neighbors_positive(vertex)
            for neighbor in neighbors:
                if distance[mate[neighbor]] == float('inf'):
                    distance[mate[neighbor]] = distance[vertex] + 1
                    queue.append(mate[neighbor])
    
    return distance[None] != float('inf')


def get_max_matching_hopcraft_karp(graph: Graph):
    distance = dict()
    mate = dict()
    for vertex in graph.vertices:
        distance[vertex] = float('inf')
        mate[vertex] = None
    max_matching = 0

    vertices_X, vertices_Y = separate_mates(graph)

    while breadth_first_hopcroft_karp(graph, vertices_X, vertices_Y, distance, mate):
        for vertex in vertices_X:
            if mate[vertex] == None:
                if depth_first_hopcroft_karp(graph, distance, mate, vertex):
                    max_matching += 1
    
    return max_matching, mate


def print_hopcroft_karp(graph: Graph) -> None:
    
    max_matching, mate = get_max_matching_hopcraft_karp(graph)

    print(f"Emparelhamento máximo: {max_matching}")
    print(f"Emparelhamentos: {mate}")
