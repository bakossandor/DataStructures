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

    def get_height(self):
        if self.left is None and self.right is None:
            return 1
        if self.left is None and self.right is not None:
            return self.right.get_height() + 1
        if self.right is None and self.left is not None:
            return self.left.get_height() + 1
        else:
            return max(self.left.get_height(), self.right.get_height()) + 1

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

    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self.root.get_height()


bst = BST()
bst.add(1)
bst.add(2)
bst.add(3)
bst.add(4)
bst.add(5)
bst.add(6)
bst.add(7)
bst.inorder_print()
print(bst.get_height())