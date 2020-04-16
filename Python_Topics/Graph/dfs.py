from utils.graph import Graph


def dfs(graph, start):
    # set to track visted nodes
    visited = set()
    dfs_path = []

    def dfs_util(graph, vertex):
        if vertex not in visited:
            dfs_path.append(vertex)
            visited.add(vertex)
            for adj_vertex in graph.vertices[vertex]:
                dfs_util(graph, adj_vertex)

    dfs_util(graph, start)

    return dfs_path


# create a graph
g = Graph()

# add edges
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'A')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'A')
g.add_edge('C', 'F')
g.add_edge('D', 'B')
g.add_edge('E', 'B')
g.add_edge('E', 'F')
g.add_edge('F', 'C')
g.add_edge('F', 'E')


print(dfs(g, 'A'))
