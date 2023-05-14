import re

from graph import Graph, Vertex, Edge
from pathlib import Path


def get_vertex(vertices: list[Vertex], label: str | int) -> Vertex:
    if isinstance(label, str):
        #print('str')
        for vertex in vertices:
            if vertex.label == label:
                return vertex
    if isinstance(label, int):
        #print("int")
        for vertex in vertices:
            if vertex.index == label:
                return vertex

    raise "Vertex label in edge invalid"


def import_graph(filepath: Path) -> Graph:
    with filepath.open() as file:
        lines = file.read().splitlines()

        if not "*vertices" in lines[0]:
            raise ('Invalid format file: not found "*vertices"')

        vertices_number = re.search("[0-9]+.?[0-9]*", lines[0])

        if vertices_number:
            vertices_number = int(vertices_number.group())
        else:
            raise ("No vertices number found")

        vertices = list()

        for index in range(vertices_number):
            vertex_index = int(lines[index + 1].split(" ")[0])
            vertex_label = lines[index + 1].split(" ")[1]
            vertex = Vertex(vertex_index, vertex_label)

            vertices.append(vertex)

        if not "*edges" in lines[vertices_number + 1]:
            raise ('Invalid format file: not found "*edges"')

        edges = list()
        weights = list()

        for index in range(vertices_number + 2, len(lines)):
            edge_label1 = lines[index].split(" ")[0]
            edge_label2 = lines[index].split(" ")[1]
            edge_weight = float(lines[index].split(" ")[2])

            if edge_weight != float("inf"):
                vertex1 = get_vertex(vertices, int(edge_label1))
                vertex2 = get_vertex(vertices, int(edge_label2))

                edge = Edge(vertex1, vertex2)
                edges.append(edge)

                weights.append(edge_weight)

        return Graph(vertices, edges, weights)
