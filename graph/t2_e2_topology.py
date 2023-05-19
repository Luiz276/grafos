from graph import Graph, Vertex, Edge

#     # A recursive function used by topologicalSort
#     def topologicalSortUtil(self,v,visited,stack):

#         # Mark the current node as visited.
#         visited[v] = True

#         # Recur for all the vertices adjacent to this vertex
#         for i in self.graph[v]:
#             if visited[i] == False:
#                 self.topologicalSortUtil(i,visited,stack)

#         # Push current vertex to stack which stores result
#         stack.insert(0,v)

#     # The function to do Topological Sort. It uses recursive
#     # topologicalSortUtil()
#     def topologicalSort(self):
#         # Mark all the vertices as not visited
#         visited = [False]*self.V
#         stack =[]

#         # Call the recursive helper function to store Topological
#         # Sort starting from all vertices one by one
#         for i in range(self.V):
#             if visited[i] == False:
#                 self.topologicalSortUtil(i,visited,stack)

# def dfs_ot(graph: Graph):
#     visited = [False]*len(graph.vertices)
#     O = []

#     for i in range(len(graph.vertices)):
#         if visited[i] == False:
#             dfs_visit_ot(graph, graph.vertices[i], visited, O)
    
#     return O

# def dfs_visit_ot(graph: Graph, v: Vertex, visited: list[bool], O: list[Vertex]):
#     visited[v.index] = True

#     for u in graph.vizinhos(v):
#         if visited[u.index-1] == False:
#             dfs_visit_ot(graph, u, visited, O)
        
#     O.insert(0, v)

def dfs_visit_ot(graph: Graph, vertex_index: int, researched: set[int], times: list[float], finals: list[float], time: int, stackO: list[Vertex]):
    researched.add(vertex_index)
    time += 1
    times[vertex_index] = time
    for u in graph.get_neighbors_positive(vertex_index):
        if u not in researched:
            dfs_visit_ot(graph, u, researched, times, finals, time, stackO)
    time += 1
    finals[vertex_index] = time
    stackO.insert(0, vertex_index)

def dfs_ot(graph: Graph):
    researched = set()      # C
    times = [float("inf")]*len(graph.vertices)         # T
    finals = [float("inf")]*len(graph.vertices)        # F
    stackO = list()         # O
    time = 0
    for v in range(len(graph.vertices)):
        if v not in researched:
            dfs_visit_ot(graph, v, researched, times, finals, time, stackO)
    
    return stackO

def print_ot(graph: Graph):
    stackO = dfs_ot(graph)
    print(stackO)
    for i in range(len(stackO)-1):
        vertex_index = stackO[i]
        print(f"{graph.get_vertex(vertex_index+1).label} -> ", end="")

    vertex_index = stackO[-1]
    print(f"{graph.get_vertex(vertex_index+1).label}")
