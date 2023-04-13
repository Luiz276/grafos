from graph import Graph, Vertex


def print_search(search: tuple[list[Vertex], list[int], int]) -> None:
    researcheds = search[0]
    depths = search[1]
    max_depth = search[2]

    # print
    for depth in range(max_depth + 1):
        vertices = list()

        for i in range(len(researcheds)):
            if depths[i] == depth:
                vertices.append(researcheds[i])

        print("Depth", depth, "vertices:", [v.label for v in vertices])


def breadth_first_search(
    graph: Graph, vertex: Vertex | str | int
) -> tuple[list[Vertex], list[int]]:
    # initialization
    vertex = graph.get_vertex(vertex)

    researcheds = [vertex]
    depths = [0]

    queue = [vertex]

    max_depth = 0

    # search
    while len(queue) > 0:
        vertex = queue.pop(0)

        current_depth = depths[researcheds.index(vertex)]

        max_depth = max(max_depth, current_depth)

        for neighbor in graph.vizinhos(vertex):
            if neighbor not in researcheds:
                researcheds.append(neighbor)
                depths.append(current_depth + 1)
                queue.append(neighbor)


def breadth_first_search_print(graph: Graph, vertex: Vertex | str | int) -> None:
    print_search(breadth_first_search(graph, vertex))
