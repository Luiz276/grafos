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

    def get_another_vertex(self, vertex: Vertex | int | str) -> Vertex:
        match vertex:
            case Vertex():
                vertex1 = self.vertex1
                vertex2 = self.vertex2
            case int():
                vertex1 = self.vertex1.index
                vertex2 = self.vertex2.index
            case str():
                vertex1 = self.vertex1.label
                vertex2 = self.vertex2.label

        if vertex == vertex1:
            return vertex2
        elif vertex == vertex2:
            return vertex1
        else:
            raise ("Vertex", vertex, "not in edge", self)


@dataclass
class Graph:
    vertices: list[Vertex]
    edges: list[Edge]
    weights: list[int | float] | None = None
    oriented: bool = False

    def get_vertex(self, vertex: str | int | Vertex):
        if type(vertex) == Vertex:
            if vertex in self.vertices:
                return vertex

        if type(vertex) == str:
            for v in self.vertices:
                if v.label == vertex:
                    return v

        if type(vertex) == int:
            for v in self.vertices:
                if v.index == vertex:
                    return v

        raise ("Invalid vertex:", vertex)

    def get_adjacency_matrix(self):
        adjacency_matrix = list()
        for vertex1 in self.vertices:
            adjacency_matrix.append(list())

            for vertex2 in self.vertices:
                edge = Edge(vertex1, vertex2)
                if edge in self.edges:
                    adjacency_matrix[-1].append(self.edges.index(edge))
                else:
                    adjacency_matrix[-1].append(float("inf"))

    def get_edges_from_a_vertex(self, vertex: Vertex) -> list[Edge]:
        edges = list()
        for edge in self.edges:
            if edge.vertex1 == vertex or edge.vertex2 == vertex:
                edges.append(edge)
        return edges

    # deprecated
    # def adjacency_matrix(self):
    #     adj_matrix = [len(self.vertices)][len(self.vertices)]
    #     for edge in self.edges:
    #         for pair in self.weights:
    #             if pair[0] == edge:
    #                 adj_matrix[edge.vertex1.index][edge.vertex2.index] = pair[1]
    #     return adj_matrix

    def qtdVertices(self) -> int:
        return len(self.vertices)

    def qtdArestas(self) -> int:
        return len(self.edges)

    def grau(self, vertex: Vertex) -> int:
        count = 0
        for edge in self.edges:
            if vertex == edge.vertex1 or vertex == edge.vertex2:
                count += 1
        return count

    def rotulo(self, index_vertex: int) -> str:
        for node in self.vertices:
            if index_vertex == node.index:
                return node.label

    # This method is mainly for not oriented graphs
    def vizinhos(self, vertex: Vertex) -> list[Vertex]:
        vizinhos = []
        for edge in self.edges:
            if vertex == edge.vertex1:
                vizinhos.append(edge.vertex2)
            elif vertex == edge.vertex2:
                vizinhos.append(edge.vertex1)
        return vizinhos

    def get_vertices_memory_index(self, vertices: list[Vertex]):
        memory_indexes = list()

        for vertex in vertices:
            memory_indexes.append(self.vertices.index(vertex))
        
        return memory_indexes
    
    # Vertex_index is the index in the list, not the number in vertex proprierties
    def get_neighbors_positive(self, vertex_index: int):
        vertex = self.vertices[vertex_index]
        neighbors = list()

        for edge in self.edges:
            if vertex == edge.vertex1:
                neighbors.append(edge.vertex2)
            
        return self.get_vertices_memory_index(neighbors)

    def haAresta(self, u: Vertex, v: Vertex) -> bool:
        for i in range(len(self.edges)):
            if (u == self.edges[i].vertex1 and v == self.edges[i].vertex2) or (
                v == self.edges[i].vertex1 and u == self.edges[i].vertex2
            ):
                if self.weights[i] != float("inf"):
                    return True
        return False

    def peso(self, u: Vertex | int | str, v: Vertex | int | str) -> float:
        u = self.get_vertex(u)
        v = self.get_vertex(v)
        for i in range(len(self.edges)):
            if (u == self.edges[i].vertex1 and v == self.edges[i].vertex2) or (
                v == self.edges[i].vertex1 and u == self.edges[i].vertex2
            ):
                return self.weights[i]

        return float("inf")
    
    def peso_by_index(self, edge: Edge):
        ind = self.edges.index(edge)
        return self.weights[ind]
