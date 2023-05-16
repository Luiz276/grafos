from graph import Graph, Vertex, Edge

def find_min(lista, graph):
    min = float("inf")
    ret = None
    for i in lista:
        ind = graph.edges.index(i)
        val = graph.weights[ind]
        if val<min:
            min = val
            ret = graph.edges[ind]
    return ret

# def find_min2(lista, graph, ver):
#     min = float("inf")
#     ret = None
#     for i in lista:
#         ind = graph.edges.index(i)
#         val = graph.weights[ind]
#         if val<min:
#             ret = i.get_another_vertex(ver)
#             min = val
#     return ret

# def prim(graph: Graph):
#     r = graph.vertices[0]
#     A = []
#     K = [float("inf")]*len(graph.vertices)
#     K[r.index-1] = 0
#     Q = graph.vertices
#     A.append(r)
#     edges = []
#     while Q != []:
#         connected_edges = graph.get_edges_from_a_vertex(r)
#         u = find_min2(connected_edges, graph, r)
#         for v in graph.vizinhos(u):
#             if v not in A and v in Q and graph.peso(u, v) < K[v.index-1]:
#                 A.append(u)
#                 K[v.index-1] = graph.peso(u,v)
#                 edges.append(Edge(u, v))
#         Q.remove(u)
#     return A, edges

# def prim2(graph: Graph):
#     #r = graph.vertices[0]
#     C = [float("inf")] * len(graph.vertices)
#     E = [0] * len(graph.vertices)
#     Q = graph.vertices
#     F = [None] * len(graph.vertices)
#     for i in range(len(graph.vertices)):
#         F[i] = [graph.vertices[i]]
#     while any(Q):
#         ind = min(C)
#         v = Q[C.index(ind)]
#         F.append(v)
#         for vw in graph.get_edges_from_a_vertex(v):
#             w = vw.get_another_vertex(v)
#             if w in Q and graph.peso_by_index(vw) < C[w.index]:
#                 C[w.index] = graph.peso_by_index(vw)
#                 E[w.index] = vw
#     return F, E

def prim3(graph: Graph):
    F = [graph.vertices[0]]
    E = []
    visited = [0]*len(graph.vertices)
    visited[0] = 1
    for _ in range(len(graph.vertices)-1):
        l = []
        for v in F:
            for edge in graph.get_edges_from_a_vertex(v):
                if visited[edge.vertex1.index-1] == 1 and visited[edge.vertex2.index-1]:
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
        visited[vr.index-1] = 1
        #print(E, "--", F)
    return E


# def print_prim(graph: Graph) -> None:
#     A, edges = prim(graph)
#     sum = 0
#     for e in edges:
#         sum += graph.weights[graph.edges.index(e)]
#     print(sum)
#     for i in range(len(edges)-1):
#         print(f"{edges[i].vertex1.index}-{edges[i].vertex2.index}, ", end="")
#     print(f"{edges[-1].vertex1.index}-{edges[-1].vertex2.index}")

def print_prim2(graph: Graph) -> None:
    E = prim3(graph)
    sum = 0
    for e in E:
        sum += graph.weights[graph.edges.index(e)]
    print(sum)
    for i in range(len(E)-1):
        print(f"{E[i].vertex1.index}-{E[i].vertex2.index}, ", end="")
    print(f"{E[-1].vertex1.index}-{E[-1].vertex2.index}")