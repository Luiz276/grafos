from graph import Graph, Vertex, Edge


def dfs_visit_ot(
    graph: Graph,
    vertex_index: int,
    researched: set[int],
    times: list[float],
    finals: list[float],
    time: int,
    stackO: list[Vertex],
):
    researched.add(vertex_index)
    time += 1
    times[vertex_index] = time
    for u in graph.get_neighbors_positive_by_inner_index(vertex_index):
        if u not in researched:
            dfs_visit_ot(graph, u, researched, times, finals, time, stackO)
    time += 1
    finals[vertex_index] = time
    stackO.insert(0, vertex_index)


def dfs_ot(graph: Graph):
    researched = set()  # C
    times = [float("inf")] * len(graph.vertices)  # T
    finals = [float("inf")] * len(graph.vertices)  # F
    stackO = list()  # O
    time = 0
    for v in range(len(graph.vertices)):
        if v not in researched:
            dfs_visit_ot(graph, v, researched, times, finals, time, stackO)

    return stackO


def print_ot(graph: Graph):
    stackO = dfs_ot(graph)
    for i in range(len(stackO) - 1):
        vertex_index = stackO[i]
        print(f"{graph.get_vertex(vertex_index+1).label} -> ", end="")

    vertex_index = stackO[-1]
    print(f"{graph.get_vertex(vertex_index+1).label}")
