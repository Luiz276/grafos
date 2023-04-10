from dataclasses import dataclass

@dataclass
class Vertice:
    index:int
    rotulo:str

@dataclass
class Oriented_edge:
    origin:Vertice
    end:Vertice

@dataclass
class Non_oriented_edge:
    vertex:set[Vertice]

@dataclass
class Graph:
    vectors:list[Vertice]
    edges:list[Non_oriented_edge]|list[Oriented_edge]
    weights:dict[Oriented_edge|Non_oriented_edge]

    def __preinit__(filename: str):
        pass

    def qtdVertices():
        pass

    def qtdArestas():
        pass

    def grau():
        pass

    def rotulo():
        pass

    def vizinhos():
        pass