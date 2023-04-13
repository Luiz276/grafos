import sys

from pathlib import Path

from reader import import_graph
from graph import Graph


def run_graph(filepath: Path) -> None:
    graph = import_graph(filepath)

    input("Press Enter to show: " + filepath.name)

    match int(sys.argv[1]):
        case 1:
            print("qtdVertices():", graph.qtdVertices())
            print("qtdArestas():", graph.qtdArestas())

            for vertex in graph.vertices:
                print("grau(" + vertex.label + "):", graph.grau(vertex.label))

            for vertex in graph.vertices:
                print("rotulo(" + vertex.label + "):", graph.rotulo(vertex.label))

            for vertex in graph.vertices:
                print("vizinhos(" + vertex.label + "):", graph.vizinhos(vertex.label))

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
            ...
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