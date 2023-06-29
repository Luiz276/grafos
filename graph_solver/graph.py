from dataclasses import dataclass


@dataclass(frozen=True)
class Vertex:
    index: int
    label: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vertex):
            return NotImplemented
        return self.index == other.index and self.label == other.label

    def __hash__(self):
        return hash(self.index)


@dataclass(frozen=True)
class Edge:
    vertex1: Vertex
    vertex2: Vertex

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Edge):
            return NotImplemented
        return (self.vertex1 == other.vertex1 and self.vertex2 == other.vertex2) or (
            self.vertex1 == other.vertex2 and self.vertex2 == other.vertex1
        )

    def get_another_vertex(self, vertex: Vertex | int | str) -> Vertex | int | str:
        match vertex:
            case Vertex():
                vertex1: Vertex | int | str = self.vertex1
                vertex2: Vertex | int | str = self.vertex2
                #print("vert")
            case int():
                vertex1 = self.vertex1.index
                vertex2 = self.vertex2.index
                #print("int")
            case str():
                vertex1 = self.vertex1.label
                vertex2 = self.vertex2.label
                #print("str")

        if vertex == vertex1:
            return vertex2
        elif vertex == vertex2:
            return vertex1
        else:
            raise Exception("Vertex", vertex, "not in edge", self)


@dataclass(frozen=True)
class Graph:
    vertices: list[Vertex]
    edges: list[Edge]
    weights: list[int | float]
    oriented: bool

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

        print("Invalid vertex:", vertex)
        raise Exception("invalid vertex")

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

        return adjacency_matrix

    def get_adjacency_matrix_capacity(self):
        adjacency_matrix = list()
        for vertex1 in self.vertices:
            adjacency_matrix.append(list())

            for vertex2 in self.vertices:
                found = False
                for i in range(len(self.edges)):
                    edge = self.edges[i]
                    if edge.vertex1 == vertex1 and edge.vertex2 == vertex2:
                        adjacency_matrix[-1].append(self.weights[i])
                        found = True
                        break
                if not found:
                    adjacency_matrix[-1].append(0)


        return adjacency_matrix

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
    def get_neighbors_positive_oriented(self, vertex: Vertex):
        neighbors = list()

        for i in range(len(self.edges)):
            edge = self.edges[i]
            if vertex == edge.vertex1:
                weight = self.weights[i]
                if weight > 0:
                    neighbors.append(edge.vertex2)

        return neighbors

    def get_neighbors_positive_not_oriented(self, vertex: Vertex):
        neighbors = list()

        for edge in self.edges:
            if vertex == edge.vertex1:
                neighbors.append(edge.vertex2)
            elif vertex == edge.vertex2:
                neighbors.append(edge.vertex1)

        return neighbors

    def get_neighbors_positive(self, vertex: Vertex):
        if self.oriented:
            return self.get_neighbors_positive_oriented(vertex)

        return self.get_neighbors_positive_not_oriented(vertex)

    # To support legacy code
    def get_neighbors_positive_by_inner_index(self, index: int):
        return self.get_vertices_memory_index(
            self.get_neighbors_positive(self.vertices[index])
        )

    def haAresta(self, u: Vertex, v: Vertex) -> bool:
        for i in range(len(self.edges)):
            if (u == self.edges[i].vertex1 and v == self.edges[i].vertex2) or (
                v == self.edges[i].vertex1 and u == self.edges[i].vertex2
            ):
                if self.weights[i] != float("inf"):
                    return True
        return False

    def peso_oriented(self, u: Vertex | int | str, v: Vertex | int | str) -> float:
        u = self.get_vertex(u)
        v = self.get_vertex(v)
        for i in range(len(self.edges)):
            if u == self.edges[i].vertex1 and v == self.edges[i].vertex2:
                return self.weights[i]

        return float("inf")

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

    def add_weight(self, edge: Edge, weight_addition: float) -> None:
        u = self.get_vertex(edge.vertex1)
        v = self.get_vertex(edge.vertex2)
        for i in range(len(self.edges)):
            if u == self.edges[i].vertex1 and v == self.edges[i].vertex2:
                self.weights[i] += weight_addition
