from graph import Graph, Vertex, Edge
from reader import import_graph


def search_minimal_path_bellman_ford(
    graph: Graph, origin_vertex: Vertex | str | int
) -> tuple[dict[float], dict[int]] | None:
    origin_vertex = graph.get_vertex(origin_vertex).index

    indexes = [vertex.index for vertex in graph.vertices]
    distances = dict()
    for index in indexes:
        distances[index] = float("inf")
    distances[origin_vertex] = 0

    antecessors = dict()

    for _ in range(graph.qtdVertices() - 1):
        for edge in graph.edges:
            vertex1 = edge.vertex1.index
            vertex2 = edge.vertex2.index

            # relaxation
            if distances[vertex1] > distances[vertex2] + graph.peso(vertex1, vertex2):
                distances[vertex1] = distances[vertex2] + graph.peso(vertex1, vertex2)
                antecessors[vertex1] = vertex2
            elif distances[vertex2] > distances[vertex1] + graph.peso(vertex2, vertex1):
                distances[vertex2] = distances[vertex1] + graph.peso(vertex2, vertex1)
                antecessors[vertex2] = vertex1

    for edge in graph.edges:
        vertex1 = edge.vertex1.index
        vertex2 = edge.vertex2.index

        # relaxation
        if distances[vertex1] > distances[vertex2] + graph.peso(vertex1, vertex2):
            return None
        elif distances[vertex2] > distances[vertex1] + graph.peso(vertex2, vertex1):
            return None

    return (distances, antecessors)


def search_minimal_path_bellman_ford_print(
    graph: Graph, origin_vertex: Vertex | str | int
) -> None:
    distances, antecessors = search_minimal_path_bellman_ford(graph, origin_vertex)

    indexes = [vertex.index for vertex in graph.vertices]

    for index in indexes:
        path = list()
        vertex = index
        while True:
            path.append(vertex)
            if vertex == origin_vertex.index:
                break
            vertex = antecessors[vertex]
        path.reverse()
        print(f"{index}: ", end="")
        print(*path, sep=",", end="")
        print(f"; d={distances[index]}")


def bellman_ford_from_file(filepath: str, origin_vertex: Vertex | str | int) -> None:
    graph = import_graph(filepath)
    search_minimal_path_bellman_ford_print(graph, origin_vertex)
