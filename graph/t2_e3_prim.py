from graph import Graph, Vertex, Edge


def find_min(lista, graph):
    min = float("inf")
    ret = None
    for i in lista:
        ind = graph.edges.index(i)
        val = graph.weights[ind]
        if val < min:
            min = val
            ret = graph.edges[ind]
    return ret


def prim3(graph: Graph):
    F = [graph.vertices[0]]
    E = []
    visited = [0] * len(graph.vertices)
    visited[0] = 1
    for _ in range(len(graph.vertices) - 1):
        l = []
        for v in F:
            for edge in graph.get_edges_from_a_vertex(v):
                if (
                    visited[edge.vertex1.index - 1] == 1
                    and visited[edge.vertex2.index - 1]
                ):
                    continue
                else:
                    l.append(edge)
        e = find_min(l, graph)
        E.append(e)
        va = e.vertex1
        vb = e.vertex2

        if va in F:
            vr = vb
        else:
            vr = va

        F.append(vr)
        visited[vr.index - 1] = 1
        # print(E, "--", F)
    return E


def print_prim2(graph: Graph) -> None:
    E = prim3(graph)
    sum = 0
    for e in E:
        sum += graph.weights[graph.edges.index(e)]
    print(sum)
    for i in range(len(E) - 1):
        print(f"{E[i].vertex1.index}-{E[i].vertex2.index}, ", end="")
    print(f"{E[-1].vertex1.index}-{E[-1].vertex2.index}")
