from graph import Graph


def floyd_warshall(graph: Graph) -> list[list[int | float | None]] | None:
    n = len(graph.vertices)  # numero de vértices no grafo
    dist = []
    for i in range(n):
        dist.append([])
        for j in range(n):
            dist[i].append(graph.peso(i + 1, j + 1))
    for k in range(n):
        for u in graph.vertices:
            for v in graph.vertices:
                dist[u.index - 1][v.index - 1] = min(
                    dist[u.index - 1][v.index - 1],
                    dist[u.index - 1][k] + dist[k][v.index - 1],
                )
    return dist


def print_floyd_warshall(graph: Graph) -> None:
    distances = floyd_warshall(graph)
    count = 0
    for line in distances:
        count += 1
        print(f"{count}:", end="")
        print(*line, sep=",")
