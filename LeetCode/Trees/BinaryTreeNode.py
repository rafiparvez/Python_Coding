class BinaryTreeNode:
    def __init__(self,rootObj):
        self.val = rootObj
        self.left = None
        self.right = None

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTreeNode(newNode)
        else:
            t = BinaryTreeNode(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTreeNode(newNode)
        else:
            t = BinaryTreeNode(newNode)
            t.right = self.right
            self.right = t


    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRootVal(self,obj):
        self.val = obj

    def getRootVal(self):
        return self.val