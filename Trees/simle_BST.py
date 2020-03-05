# implementing a simple "inbalanced" BST

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add(self, data):
        if data < self.data:
            if self.left is not None:
                self.left.add(data)
            else:
                self.left = Node(data)
        else:
            if self.right is not None:
                self.right.add(data)
            else:
                self.right = Node(data)

    def inorder_print(self):
        if self.left is not None:
            self.left.inorder_print()
        print(self.data)
        if self.right is not None:
            self.right.inorder_print()

class BST:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.add(data)

    def inorder_print(self):
        if self.root is None:
            return False
        else:
            self.root.inorder_print()


bst = BST()
bst.add(123)
bst.add(234)
bst.add(0)
bst.add(-23)
bst.add(23123)
bst.add(2)
bst.add(231)
bst.inorder_print()