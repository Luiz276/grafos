from dataclasses import dataclass

@dataclass
class Vertice:
    index:int
    label:str

    def __eq__(self, __value: object) -> bool:
        return self.index==__value.index and self.label==__value.label

@dataclass
class Edge:
    vertex1:Vertice
    vertex2:Vertice
    
    def __eq__(self, __value: object) -> bool:
        return (self.vertex1==__value.vertex1 and self.vertex2==__value.vertex2) or (self.vertex1==__value.vertex2 and self.vertex2==__value.vertex1)

@dataclass
class Graph:
    vectors:list[Vertice]
    edges:list[Edge]
    weights:dict[Edge]

    def __preinit__(filename: str):
        pass

    def qtdVertices(self):
        return len(self.vectors)

    def qtdArestas(self):
        return len(self.edges)

    def grau(self):
        pass

    def rotulo(self):
        pass

    def vizinhos(self):
        pass

    def haAresta(self):
        pass

    def peso(self):
        pass