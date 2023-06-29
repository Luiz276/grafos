from graph import Graph, Vertex, Edge

def conjuntosIndMax():
    pass


# def color(graph: Graph):
#     n_vertices = graph.qtdVertices()
#     #print(n_vertices)

#     X = [-1] * ((2**n_vertices)-1)
#     X[0] = 0
#     #S = [0]

#     #available = [False] * n_vertices
#     for u in range(1, 2**n_vertices):
#         X[u] = float("inf")

def color(graph: Graph):
    vertices = sorted(graph.vertices, key=lambda obj: len(graph.vizinhos(obj)), reverse=True)
    colour_graph = {}

    for vertex in vertices:
        unused_colours = len(vertices) * [True]
        for neighbor in graph.vizinhos(vertex):
            if neighbor.index in colour_graph:
                colour = colour_graph[neighbor.index]
                unused_colours[colour] = False
        for colour, unused in enumerate(unused_colours):
            if unused:
                colour_graph[vertex.index] = colour
                break
    return colour_graph

def print_vertex_coloring(graph: Graph) -> None:
    res = color(graph)
    #res.sort()
    n_cromatico = max(res.values())+1
    for i in range(1,len(graph.vertices)+1):
        print(f"Vértice {i} -> cor {res[i]}")
    print(f"Número cromático: {n_cromatico}")
