from graph import Graph, Edge, Vertex


def search_breadth_first_edmonds_karp(
    residual_network: Graph, source: Vertex, sink: Vertex
) -> tuple[list[Vertex], int] | None:
    antecessors = dict()

    visited_vertexes = {source}
    queue = [source]
    while len(queue) > 0:
        vertex = queue.pop(0)
        for neighbor in residual_network.get_neighbors_positive(vertex):
            if (
                neighbor not in visited_vertexes
                and residual_network.peso(vertex, neighbor) > 0
            ):
                visited_vertexes.add(neighbor)
                antecessors[vertex] = neighbor

                if neighbor == sink:
                    max_local_flux = float("inf")
                    augmented_path = [sink]
                    current = sink
                    while current != source:
                        antecessor = antecessors[current]
                        augmented_path = [antecessor] + augmented_path

                        max_local_flux = min(
                            max_local_flux, residual_network.peso(antecessor, current)
                        )
                        current = antecessor
                    return augmented_path, max_local_flux

    return None


def check_valid_network(adjacency_matrix: list[list[float]]) -> bool:
    for i in range(len(adjacency_matrix)):
        for j in range(i, len(adjacency_matrix)):
            if i != j:
                weight_vu = adjacency_matrix[i][j]
                weight_uv = adjacency_matrix[j][i]
                if abs(weight_vu - weight_uv) != max(abs(weight_vu), abs(weight_uv)):
                    raise Exception(f"Invalid edges for network, i = {i} and j = {j}")
            elif adjacency_matrix[i][i] != 0:
                raise Exception(f"Invalid network, cycle with i = {i}")

    return True


def generate_residual_network(graph: Graph) -> Graph:
    adjacency_matrix = graph.get_adjacency_matrix_capacity()

    # Poderia ser incorporado com os laços de repetição a seguir, mas assim é mais didático
    check_valid_network(adjacency_matrix)

    residual_flux_edges = list()
    residual_flux_weights = list()
    used_flux_edges = list()
    used_flux_weights = list()

    for i in range(len(adjacency_matrix)):
        for j in range(i, len(adjacency_matrix)):
            if i == j:
                edge_vv = Edge(graph.vertices[i], graph.vertices[i])

                residual_flux_edges.append(edge_vv)
                residual_flux_weights.append(0)
            else:
                weight_vu = adjacency_matrix[i][j]
                weight_uv = adjacency_matrix[j][i]
                edge_vu = Edge(graph.vertices[i], graph.vertices[j])
                edge_uv = Edge(graph.vertices[j], graph.vertices[i])

                if weight_uv > weight_vu:
                    residual_flux_edges.append(edge_uv)
                    residual_flux_weights.append(weight_uv)
                    used_flux_edges.append(edge_vu)
                    used_flux_weights.append(0)

                else:
                    residual_flux_edges.append(edge_vu)
                    residual_flux_weights.append(weight_vu)
                    used_flux_edges.append(edge_uv)
                    used_flux_weights.append(0)

    residual_network = Graph(
        graph.vertices,
        residual_flux_edges + used_flux_edges,
        residual_flux_weights + used_flux_weights,
        True,
    )

    return residual_network


def get_max_flux_edmonds_karp(graph: Graph, source: Vertex, sink: Vertex) -> int:
    max_flux = 0

    residual_network = generate_residual_network(graph)

    while True:
        path_founded = search_breadth_first_edmonds_karp(residual_network, source, sink)
        if path_founded is None:
            return max_flux

        augmented_path, max_local_flux = path_founded
        max_flux += max_local_flux

        for i in range(len(augmented_path) - 1):
            edge = Edge(augmented_path[i], augmented_path[i + 1])
            residual_network.add_weight(edge, max_local_flux)
            edge = Edge(augmented_path[i + 1], augmented_path[i])
            residual_network.add_weight(edge, max_local_flux)


def print_edmonds_karp(
    graph: Graph, source: Vertex | None = None, sink: Vertex | None = None
) -> None:
    if source == None:
        source = graph.vertices[0]
    if sink == None:
        sink = graph.vertices[-1]

    max_flux = get_max_flux_edmonds_karp(graph, source, sink)

    print(f"Fluxo máximo entre {source.label} e {sink.label}: {max_flux}")
