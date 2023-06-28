from graph import Graph, Edge


def find_min(edges: list[Edge], graph: Graph):
    min_value = float("inf")
    min_edge = None
    for edge in edges:
        index = graph.edges.index(edge)
        value = graph.weights[index]
        if value < min_value:
            min_value = value
            min_edge = graph.edges[index]
    return min_edge


def prim3(graph: Graph):
    vertices_in_tree_generator = [graph.vertices[0]]
    edges_in_tree_generator = []

    # Percore até que vertices_in_tree_generator compreenda todos os vértices do grafo
    for _ in range(len(graph.vertices) - 1):
        edges_to_expand_tree_generator = []
        for v in vertices_in_tree_generator:
            for edge in graph.get_edges_from_a_vertex(v):
                if (
                    edge.vertex1 in vertices_in_tree_generator
                    and edge.vertex2 in vertices_in_tree_generator
                ):
                    continue
                else:
                    edges_to_expand_tree_generator.append(edge)
        edge_to_expand = find_min(edges_to_expand_tree_generator, graph)
        edges_in_tree_generator.append(edge_to_expand)
        v = edge_to_expand.vertex1
        u = edge_to_expand.vertex2

        if v in vertices_in_tree_generator:
            new_vertex_reached = u
        else:
            new_vertex_reached = v

        vertices_in_tree_generator.append(new_vertex_reached)

    return edges_in_tree_generator


def print_prim2(graph: Graph) -> None:
    edges_in_tree_generator = prim3(graph)
    sum = 0
    for edge_to_expand in edges_in_tree_generator:
        sum += graph.weights[graph.edges.index(edge_to_expand)]
    print(sum)
    for edge in edges_in_tree_generator[:-1]:
        print(
            f"{edge.vertex1.index}-{edge.vertex2.index}, ",
            end="",
        )
    print(
        f"{edges_in_tree_generator[-1].vertex1.index}-{edges_in_tree_generator[-1].vertex2.index}"
    )
