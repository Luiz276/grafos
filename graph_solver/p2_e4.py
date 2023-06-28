from graph import Graph, Vertex, Edge


def get_neighbors_positive_p2(self, vertex_index: int):
    vertex = self.vertices[vertex_index]
    neighbors = list()

    for edge in self.edges:
        if vertex == edge.vertex1:
            neighbors.append(edge.vertex2)

    return neighbors


def algorithm_17(graph: Graph, v: Vertex, C, T, A, F, time):
    C[v.index]
    time += 1
    T[v.index] = time
    for u in graph.get_neighbors_positive_p2(graph.vertices.index(v)):
        if C[u.index] == False:
            A[u.index] = v.index
            time = algorithm_17(graph, u, C, T, A, F, time)
    time += 1
    F[v.index] = time
    return time


def algorithm_16(graph: Graph):
    C = [False for v in graph.vertices]
    T = [float("inf") for v in graph.vertices]
    F = [float("inf") for v in graph.vertices]
    A = [None for v in graph.vertices]

    time = 0

    for u in graph.vertices:
        if C[u.index] == False:
            algorithm_17(graph, u, C, T, A, F, time)

    return C, T, A, F


def dfs_visit(graph: Graph, v: Vertex, C, A):
    C[v.index]
    for u in graph.get_neighbors_positive_p2(graph.vertices.index(v)):
        if C[u.index] == False:
            A[u.index] = v.index
            dfs_visit(graph, u, C, A)


def dfs(graph: Graph, s: int):
    C = [False for v in graph.vertices]
    A = [None for v in graph.vertices]

    u = graph.vertices[s]
    dfs_visit(graph, u, C, A)

    return C, A


def graph_example():
    a = Vertex(0, "a")
    b = Vertex(1, "b")
    c = Vertex(2, "c")
    d = Vertex(3, "d")
    e = Vertex(4, "e")
    x = Vertex(5, "f")
    y = Vertex(6, "y")
    w = Vertex(7, "w")
    z = Vertex(8, "z")
    v = [a, b, c, d, e, x, y, w, z]

    ab = Edge(a, b)
    bd = Edge(b, d)
    de = Edge(d, e)
    # ae = Edge(a, e)
    # ac = Edge(a, c)
    # bc = Edge(b, c)
    cd = Edge(c, d)

    xy = Edge(x, y)
    wy = Edge(w, y)
    wz = Edge(w, z)
    # yz = Edge(y, z)

    bx = Edge(b, x)
    dw = Edge(d, w)
    ez = Edge(e, z)

    # edges = [ab, bd, de, cd, xy, wy, wz, bx, dw, ez]
    edges = [ab, bd, de, cd, xy, wy, wz]
    # edges = [ab, bd, de, ae, ac, bc, cd, xy, wy, wz, yz]

    return Graph(
        v,
        edges,
        [5] * 7,
        # [5]*7 + [1]*3,
        False,
    )


def test():
    graph = graph_example()
    # C, T, A, F = algorithm_16(graph)
    C, A = dfs(graph, 3)
    print("Fim")


"""
G1 = (V', E', w') 
G2 = (V'', E'', w'') 

G3 <- (V' U V'', E' U E'' U A, w3)

r <- selecionar uma aresta arbitrária de A

T3 <- T' U T'' U {r}
H <- (V' U V'', T3, w3)

A <- A/r

for {v, u} in A
    C, T, A', F <- DFS-modificado(H, v)
    a <- {v,u}
    m <- w3({v,u})
    y <- u
    while y != v
        x <- A'y
        if w3({x,y}) > m
            a <- {x,y}
            m <- w3({x,y})
    
    T3 <- T3 U {{v,u}}   # Atualiza as arestas do grafo temporário H que corresponderá no final à árvore geradora mínima de G3
    T3 <- T3/{a}         # Remove a aresta desnecessária mais cara

return T3

A ideia do algoritmo é inicialmente unir a duas árvores geradoras que já se tem, depois adicionar uma aresta do conjunto de A por vez.
Para cada aresta adicionada (com exceção da primeira) uma aresta é retirada. 
Será retirado a aresta mais cara das que estão num dos ambos caminhos que conectam os vértices da última aresta adicionada.
Um caminho é a nova aresta e o outro caminho é o único que existia até então e é encontrado através de uma busca em profundidade.

DFS-modificado(H, v) corresponde ao algoritmo 16, com um vértice s a mais como parametro e com as linhas 6 e 7 substítuidas pela única seguinte linha:
u <- s
"""
