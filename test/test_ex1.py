from graph.graph import Graph, Vertice, Edge

def initGraph():
    a = Vertice(1,"a")
    b = Vertice(2,"b")
    c = Vertice(3,"c")
    d = Vertice(4,"d")
    v = [a,b,c,d]
    ab = Edge(a,b)
    bc = Edge(b,c)
    ca = Edge(c,a)
    bd = Edge(b,d)
    e = [ab, bc, ca, bd]
    w = [(ab,7), (bc, 13), (ca, 22), (bd, 3)]
    return Graph(v,e,w)

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
    graph =initGraph()
    output = graph.grau("b")
    expected_output = 3
    assert output == expected_output

def test_rotulo():
    graph = initGraph()
    output = graph.rotulo(2)
    expected_output = "b"
    assert output == expected_output

def test_vizinhos():
    graph = initGraph()
    output = graph.vizinhos("b")
    expected_output = {"a", "c", "d"}
    assert output == expected_output

def test_haAresta_true():
    graph = initGraph()
    output = graph.haAresta("a","b")
    expected_output = True
    assert output == expected_output

def test_haAresta_false():
    graph = initGraph()
    output = graph.haAresta("a","d")
    expected_output = False
    assert output == expected_output

def test_peso_inf():
    graph = initGraph()
    output = graph.peso("a","d")
    expected_output = float('inf')
    assert output == expected_output

def test_peso_num():
    graph = initGraph()
    output = graph.peso("a","b")
    expected_output = 7
    assert output == expected_output

def test_ler():
    output = Graph("graph1.txt")
    expected_output = initGraph()
    assert output == expected_output