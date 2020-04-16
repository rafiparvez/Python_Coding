from utils.graph import Graph


def top_sort(graph):
    visited = set()
    stack = []

    def top_sort_util(graph, vertex):

        if vertex not in visited:
            visited.add(vertex)

            for adj_vertex in graph.vertices[vertex]:
                top_sort_util(graph, adj_vertex)
            stack.append(vertex)

    for v in list(graph.vertices.keys()):
        top_sort_util(graph, v)

    result = []
    while stack:
        result.append(stack.pop())

    return result


g = Graph()

g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('E', 'D')

print(top_sort(g))
