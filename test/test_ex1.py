from pathlib import Path

from graph.graph import Graph, Vertex, Edge
from graph.reader import import_graph


# graph1.txt
def initGraph():
    a = Vertex(1, "a")
    b = Vertex(2, "b")
    c = Vertex(3, "c")
    d = Vertex(4, "d")
    v = [a, b, c, d]
    ab = Edge(a, b)
    ac = Edge(a, c)
    bc = Edge(b, c)
    bd = Edge(b, d)
    e = [ab, ac, bc, bd]
    w = [7.0, 13.0, 22.0, 3.0]
    return Graph(v, e, w)


def test_qtdVertices():
    graph = initGraph()
    output = graph.qtdVertices()
    expected_output = 4
    assert output == expected_output


def test_qtdArestas():
    graph = initGraph()
    output = graph.qtdArestas()
    expected_output = 4
    assert output == expected_output


def test_grau():
    graph = initGraph()
    output = graph.grau(Vertex(2, "b"))
    expected_output = 3
    assert output == expected_output


def test_rotulo():
    graph = initGraph()
    output = graph.rotulo(2)
    expected_output = "b"
    assert output == expected_output


def test_vizinhos():
    graph = initGraph()
    output = graph.vizinhos(Vertex(2, "b"))
    expected_output = [Vertex(1, "a"), Vertex(3, "c"), Vertex(4, "d")]
    assert output == expected_output


def test_haAresta_true():
    graph = initGraph()
    output = graph.haAresta(Vertex(1, "a"), Vertex(2, "b"))
    expected_output = True
    assert output == expected_output


def test_haAresta_false():
    graph = initGraph()
    output = graph.haAresta(Vertex(1, "a"), Vertex(4, "d"))
    expected_output = False
    assert output == expected_output


def test_peso_inf():
    graph = initGraph()
    output = graph.peso(Vertex(1, "a"), Vertex(4, "d"))
    expected_output = float("inf")
    assert output == expected_output


def test_peso_num():
    graph = initGraph()
    output = graph.peso(Vertex(1, "a"), Vertex(2, "b"))
    expected_output = 7
    assert output == expected_output


def test_ler_graph1():
    path = Path().resolve(__file__)
    filepath = path / "test" / "graph1.txt"

    output = import_graph(filepath)
    expected_output = initGraph()
    assert output == expected_output
