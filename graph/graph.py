from dataclasses import dataclass


@dataclass
class Vertex:
    index: int
    label: str

    def __eq__(self, __value: object) -> bool:
        return self.index == __value.index and self.label == __value.label


@dataclass
class Edge:
    vertex1: Vertex
    vertex2: Vertex

    def __eq__(self, __value: object) -> bool:
        return (
            self.vertex1 == __value.vertex1 and self.vertex2 == __value.vertex2
        ) or (self.vertex1 == __value.vertex2 and self.vertex2 == __value.vertex1)


@dataclass
class Graph:
    vertices: list[Vertex]
    edges: list[Edge]
    weights: list[int | float]

    def adjacency_matrix(self):
        adj_matrix = [len(self.vertices)][len(self.vertices)]
        for edge in self.edges:
            for pair in self.weights:
                if pair[0] == edge:
                    adj_matrix[edge.vertex1.index][edge.vertex2.index] = pair[1]
        return adj_matrix

    @classmethod
    def fromfilename(self, filename: str):
        vertices = []
        edges = []
        weights = []
        file = open(filename)
        bool_edge = False
        for linha in file:
            if linha[:-3] == "*vertices":
                n_vert = int(linha[-2:])
            elif n_vert > 0:
                n_vert -= 1
                items = linha.split()
                vertices.append(Vertex(int(items[0]), items[1]))
            elif linha.rstrip() == "*edges":
                bool_edge = True
            elif bool_edge == True:
                edge = Edge(linha[0], linha[2])
                edges.append(edge)
                weights.append((edge, int(linha[4:])))
        return Graph(vertices, edges, weights)

    def qtdVertices(self) -> int:
        return len(self.vertices)

    def qtdArestas(self) -> int:
        return len(self.edges)

    def grau(self, vertice: Vertex) -> int:
        count = 0
        for edge in self.edges:
            if vertice == edge.vertex1 or vertice == edge.vertex2:
                count += 1
        return count

    def rotulo(self, index_vertice: int) -> str:
        for node in self.vertices:
            if index_vertice == node.index:
                return node.label

    def vizinhos(self, vertice: Vertex):
        vizinhos = []
        for edge in self.edges:
            if vertice == edge.vertex1:
                vizinhos.append(edge.vertex2)
            elif vertice == edge.vertex2:
                vizinhos.append(edge.vertex1)
        return vizinhos

    def haAresta(self, u: Vertex, v: Vertex):
        for i in range(len(self.edges)):
            if (u == self.edges[i].vertex1 and v == self.edges[i].vertex2) or (v == self.edges[i].vertex1 and u == self.edges[i].vertex2):
                if self.weights[i] != float("inf"):
                    return True
        return False

    def peso(self, u: Vertex, v: Vertex):
        for i in range(len(self.edges)):
            if (u == self.edges[i].vertex1 and v == self.edges[i].vertex2) or (v == self.edges[i].vertex1 and u == self.edges[i].vertex2):
                return self.weights[i]

        return float("inf")