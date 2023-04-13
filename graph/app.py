import sys

from pathlib import Path

from reader import import_graph
from graph import Graph
from t1_e2_breadth_first import breadth_first_search_print


def run_graph(filepath: Path) -> None:
    graph = import_graph(filepath)

    # input("Press Enter to show: " + filepath.name)

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
            breadth_first_search_print(graph, graph.vertices[0])

        case 3:
            ...

        case 4:
            ...

        case 5:
            ...

        case 6:
            ...


def main() -> None:
    if len(sys.argv) < 2:
        raise ("run SCRIPT OPTION [FILES]")

    path = Path(__file__).parents[1]

    if len(sys.argv) < 3:
        filepath = path / "test" / "graph1.txt"
        run_graph(filepath)
    else:
        for arg in sys.argv[2:]:
            filepath = path / arg
            run_graph(filepath)
