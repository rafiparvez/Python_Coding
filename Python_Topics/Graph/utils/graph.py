"""
The Graph Class
"""

from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertices = defaultdict(list)

    def add_edge(self, v, e):
        self.vertices[v].append(e)




