def initGraph():
    v = {"a", "b", "c", "d"}
    e = {{"a", "b"}, {"b", "c"}, {"c", "a"}, {"b", "d"}}
    w = dict()
    w[{"a", "b"}] = 7
    w[{"b", "c"}] = 23
    w[{"c", "a"}] = 12
    w[{"b", "d"}] = 3
    grafo = Grafo(v,e,w)
    return grafo

def test_qtdVertices():
    grafo = initGraph()
    output = grafo.qtdVertices()
    expected_output = 4
    assert output == expected_output

def test_qtdArestas():
    grafo = initGraph()
    output = grafo.qtdArestas()
    expected_output = 4
    assert output == expected_output

def test_grau():
    grafo =initGraph()
    output = grafo.grau("b")
    expected_output = 3
    assert output == expected_output

def test_rotulo():
    grafo = initGraph()
    output = grafo.rotulo("b")
    expected_output = "b"
    assert output == expected_output

def test_vizinhos():
    grafo = initGraph()
    output = grafo.vizinhos("b")
    expected_output = {"a", "c", "d"}
    assert output == expected_output

def test_haAresta_true():
    grafo = initGraph()
    output = grafo.haAresta("a","b")
    expected_output = True
    assert output == expected_output

def test_haAresta_false():
    grafo = initGraph()
    output = grafo.haAresta("a","d")
    expected_output = False
    assert output == expected_output

def test_peso_inf():
    grafo = initGraph()
    output = grafo.peso("a","d")
    expected_output = NaN
    assert output == expected_output

def test_peso_num():
    grafo = initGraph()
    output = grafo.peso("a","b")
    expected_output = 7
    assert output == expected_output

def test_ler():
    output = Grafo(grafo1.txt)
    expected_output = initGraph()
    assert output == expected_output