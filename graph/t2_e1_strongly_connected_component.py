from graph import Graph, Vertex, Edge


def depth_first_search_visit(
    graph: Graph,
    vertex_index: int,
    researched: set[int],
    times: list[float],
    finals: list[float],
    antecessors: list[int | None],
    time: int,
):
    researched.add(vertex_index)
    time += 1
    times[vertex_index] = time
    for u in graph.get_neighbors_positive(vertex_index):
        if u not in researched:
            antecessors[u] = vertex_index
            time = depth_first_search_visit(
                graph, u, researched, times, finals, antecessors, time
            )
    time += 1
    finals[vertex_index] = time
    return time


def depth_first_search(graph: Graph):
    researched = set()  # C
    times = list()  # T
    finals = list()  # F
    antecessors = list()  # A
    for _ in range(len(graph.vertices)):
        times.append(float("inf"))
        finals.append(float("inf"))
        antecessors.append(None)
    time = 0
    for v in range(len(graph.vertices)):
        if v not in researched:
            depth_first_search_visit(
                graph, v, researched, times, finals, antecessors, time
            )

    return antecessors, finals


def transpose_list(l: list[int]) -> list:
    d = dict()
    for i in range(len(l)):
        d[l[i]] = i

    new_l = list()
    for i in range(len(l)):
        new_l.append(dict[i])

    return new_l


def transpose_edges(edges: list[Edge]) -> list[Edge]:
    edges_transposed = list()
    for edge in edges:
        edges_transposed.append(Edge(edge.vertex2, edge.vertex1))

    return edges_transposed


def sort_vertices_by_final_times_only_index(finals: list[int]) -> list[int]:
    return sorted(range(len(finals)), key=lambda k: finals[k], reverse=True)


def sort_vertices_by_final_times(
    vertices: list[Vertex], finals: list[int]
) -> list[int]:
    new_order = sort_vertices_by_final_times_only_index(finals)

    new_vertices = list()

    for i in new_order:
        new_vertices.append(vertices[i])

    return new_vertices


def search_strongly_connected_components(graph: Graph):
    _, finals = depth_first_search(graph)

    edges_transposed = transpose_edges(graph.edges)

    new_vertices = sort_vertices_by_final_times(graph.vertices, finals)

    new_graph = Graph(new_vertices, edges_transposed, None, True)

    antecessors, finals = depth_first_search(new_graph)

    return new_vertices, antecessors, finals


def separate_strongly_connected_components(
    antecessors: list[int], finals: list[int]
) -> list[set[int]]:
    new_order = sort_vertices_by_final_times_only_index(finals)

    components = [{new_order[0]}]

    for i in new_order[1:]:
        if antecessors[i] is None:
            components.append({i})
        else:
            for component in components:
                if antecessors[i] in component:
                    component.add(i)

    return components


def print_components(vertices: list[Vertex], components: list[set[Vertex]]) -> None:
    for component in components:
        print(*[vertices[i].index for i in component], sep=",")


def search_and_print_strongly_connected_components(graph: Graph):
    vertices, antecessors, finals = search_strongly_connected_components(graph)

    separated_components = separate_strongly_connected_components(antecessors, finals)

    print_components(vertices, separated_components)
