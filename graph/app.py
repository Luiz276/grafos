import sys

from pathlib import Path

from reader import import_graph
from graph import Graph
from t1_e2_breadth_first import breadth_first_search_print
from t1_e3_eulerian_cycle import eulerian_cycle_print
from t1_e4_bellman_ford import search_minimal_path_bellman_ford_print
from t1_e5_floyd_warshall import print_floyd_warshall
from t2_e3_prim import print_prim2
from t2_e2_topology import print_ot
from t2_e1_strongly_connected_component import (
    search_and_print_strongly_connected_components,
)


def run(graph: Graph, vertex: str | None) -> None:
    match int(sys.argv[1]):
        case 1:
            print("qtdVertices():", graph.qtdVertices())
            print("qtdArestas():", graph.qtdArestas())

            for vertex in graph.vertices:
                print("grau(" + vertex.label + "):", graph.grau(vertex))

            for vertex in graph.vertices:
                print("rotulo(" + str(vertex.index) + "):", graph.rotulo(vertex.index))

            for vertex in graph.vertices:
                print(
                    "vizinhos(" + vertex.label + "):",
                    [neighbor.label for neighbor in graph.vizinhos(vertex)],
                )

            for vertex1 in graph.vertices:
                for vertex2 in graph.vertices:
                    print(
                        "haAresta(" + vertex1.label + ", " + vertex2.label + "):",
                        graph.haAresta(vertex1, vertex2),
                    )

            for vertex1 in graph.vertices:
                for vertex2 in graph.vertices:
                    print(
                        "peso(" + vertex1.label + ", " + vertex2.label + "):",
                        graph.peso(vertex1, vertex2),
                    )

        case 2:
            if not vertex:
                vertex = graph.vertices[0]
            else:
                if vertex.isdigit():
                    vertex = int(vertex)  # search by index

                    # else search by label

                vertex = graph.get_vertex(vertex)

            breadth_first_search_print(graph, vertex)

        case 3:
            eulerian_cycle_print(graph)

        case 4:
            if not vertex:
                vertex = graph.vertices[0]
            else:
                if vertex.isdigit():
                    vertex = int(vertex)  # search by index

                    # else search by label

                vertex = graph.get_vertex(vertex)
            search_minimal_path_bellman_ford_print(
                graph, vertex
            )  # TODO: mudar para qualquer vertice

        case 5:
            print_floyd_warshall(graph)

        case 6:
            # t2_e1
            search_and_print_strongly_connected_components(graph)

        case 7:
            # t2_e2
            print_ot(graph)

        case 8:
            # t2_e3
            print_prim2(graph)


def main() -> None:
    if len(sys.argv) < 2:
        raise ("run SCRIPT OPTION [FILES]")

    path = Path(__file__).parents[1]

    if int(sys.argv[1]) == 2 or int(sys.argv[1]) == 4:
        vertex = sys.argv[2]
        files = sys.argv[3:]
    else:
        vertex = None
        files = sys.argv[2:]

    if not files:
        filepath = path / "test" / "graph1.txt"
        graph = import_graph(filepath)
        run(graph, vertex)
    else:
        if len(files) == 1:
            filepath = path / files[0]
            graph = import_graph(filepath)
            run(graph, vertex)
        else:
            for arg in files:
                graph = import_graph(filepath)
                filepath = path / arg
                input("Press Enter to show: " + filepath.name)
                run(graph, vertex)
