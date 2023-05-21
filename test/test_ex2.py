from graph.graph import Graph, Vertex, Edge
from graph.t2_e1_strongly_connected_component import (
    depth_first_search,
    sort_vertices_by_final_times,
    search_and_print_strongly_connected_components,
)


def initGraph3():
    a = Vertex(1, "a")  # 0
    b = Vertex(2, "b")  # 1
    c = Vertex(3, "c")  # 2
    d = Vertex(4, "d")  # 3
    e = Vertex(5, "e")  # 4
    f = Vertex(6, "f")  # 5
    v = [a, b, c, d, e, f]
    ab = Edge(a, b)
    bd = Edge(b, d)
    dc = Edge(d, c)
    ca = Edge(c, a)
    bf = Edge(b, f)
    fe = Edge(f, e)
    ef = Edge(e, f)
    de = Edge(d, e)
    edges = [ab, bd, dc, ca, bf, fe, ef, de]
    return Graph(v, edges, None, oriented=True)


def test_depth_first_search():
    graph = initGraph3()
    antecessors, finals = depth_first_search(graph)
    assert antecessors == finals


def test_sort_vertices_by_final_times():
    graph = initGraph3()
    finals = [1, 2, 8, 4, 9, 6]
    a = Vertex(1, "a")
    b = Vertex(2, "b")
    c = Vertex(3, "c")
    d = Vertex(4, "d")
    e = Vertex(5, "e")
    f = Vertex(6, "f")
    expected_new_vertices = [e, c, f, d, b, a]
    new_vertices = sort_vertices_by_final_times(graph.vertices, finals)
    assert new_vertices == expected_new_vertices


def test_strongly_connected_components():
    graph = initGraph3()

    search_and_print_strongly_connected_components(graph)
