class Node:
    def __init__(self,data):
        self.data = data
        self.children = []


def diameter(Tree):
    dia=0
    def getdepth(Tree):
        nonlocal dia
        top2depth = [0, 0]
        if not Tree:
            return 0
        for child in Tree.children:
            depth = getdepth(child) + 1
            if depth > top2depth[0]:
                top2depth[0], top2depth[1] = depth, top2depth[0]
            elif depth >top2depth[1]:
                top2depth[1] = depth
        dia = max(dia, top2depth[0]+top2depth[1]+1)
        return top2depth[0]
    getdepth(Tree)
    return dia

'''  Let us create below tree
               A
             / /  \  \
           B  C   D  E
          / \     |  
         F  G    H
        /   
       I
 '''

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I= Node('I')

A.children=[B,C,D,E]
B.children = [F,G]
D.children = [H]
F.children = [I]

print("Diameter of given binary tree is %d" % (diameter(A)))