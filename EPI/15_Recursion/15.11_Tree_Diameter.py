#Time_Complexity

import collections
class Node:
    def __init__(self):
        self.children = []

Edge = collections.namedtuple('Edge', ('length', 'childNode'))

def diameter(Tree):
    dia = 0
    def getDepth(Tree):
        top2Depths = [0,0]
        nonlocal dia
        if not (Tree.children):
            return 0 # return 0 depth
        for edge in Tree.children:
            depth = getDepth(edge.childNode)+edge.length
            if depth >top2Depths[0]:
                top2Depths[0], top2Depths[1]=depth, top2Depths[0]
            elif depth >top2Depths[1]:
                top2Depths[1] = depth
        dia=max(dia, top2Depths[0]+top2Depths[1])
        return top2Depths[0] # depth of a tree is max depth among all subtrees

    getDepth(Tree)
    return dia

"""
Testing the code for following Binary Tree:

Constructed binary tree is 
            A
          /1  \2 \3
        B      C  F
      /4  \5
    D     E

"""

A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
A.children = [Edge(length=1, childNode=B), Edge(length=2, childNode=C), Edge(length=3, childNode=C)]
B.children = [Edge(length=4, childNode=D), Edge(length=5, childNode=E)]

print("Diameter of given binary tree is %d" % (diameter(A)))