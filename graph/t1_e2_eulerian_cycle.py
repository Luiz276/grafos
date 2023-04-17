from graph import Graph, Vertex, Edge

def eulerian_subcycle(graph: Graph, vertex: Vertex, edges_reached: list[Edge]) -> tuple[list[Vertex] | None, list[Edge]]:
    subcycle = [vertex]

    while True:
        has_unreached_edge = False
        for edge in graph.get_edges_from_a_vertex(vertex):
            if edge not in edges_reached:
                has_unreached_edge = True
                edges_reached.append(edge)
                if edge.vertex1 == vertex:
                    vertex = edge.vertex2
                else:
                    vertex = edge.vertex1
                subcycle.append(vertex)
                break

        if has_unreached_edge == False:
            return None
        
        if vertex == subcycle[0]:
            return subcycle, edges_reached
    
def eulerian_cycle(graph: Graph) -> list[Vertex] | None:
    vertex = graph.vertices[0]

    edges_reached = list()

    cycle = eulerian_subcycle(graph, vertex, edges_reached)

    if cycle is None:
        return None

    if len(edges_reached) != len(graph.edges):
        for index in range(len(cycle)):
            vertex = cycle[index]
            for edge in graph.get_edges_from_a_vertex(vertex):
                if edge not in edges_reached:
                    subcycle, edges_reached = eulerian_subcycle(graph, vertex, edges_reached)
                    if subcycle is None:
                        return None

                    cycle = cycle[:index] + subcycle + cycle[index + 1:]
    
    if len(edges_reached) != len(graph.edges):
        return None
    
    return cycle