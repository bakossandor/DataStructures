# simple implementation of BST

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if data == self.data:
            return False
        elif data < self.data:
            if self.left_child is not None:
                self.left_child.insert(data)
            else:
                self.left_child = Node(data)
        elif data > self.data:
            if self.right_child is not None:
                self.right_child.insert(data)
            else:
                self.right_child = Node(data)

    def inorder(self):
        if self.left_child is not None:
            self.left_child.inorder()
        print(self.data)
        if self.right_child is not None:
            self.right_child.inorder()

    def postorder(self):
        if self.right_child is not None:
            self.right_child.postorder()
        print(self.data)
        if self.left_child is not None:
            self.left_child.postorder()

    def preorder(self):
        print(self.data)
        if self.left_child is not None:
            self.left_child.preorder()
        if self.right_child is not None:
            self.right_child.preorder()

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is not None:
            self.root.insert(data)
        else:
            self.root = Node(data)

    def inorder(self):
        if self.root is not None:
            self.root.inorder()
        else:
            return False

    def postorder(self):
        if self.root is not None:
            self.root.postorder()
        else:
            return False

    def preorder(self):
        if self.root is not None:
            self.root.preorder()
        else:
            return False

    def remove(self, data):
        if self.root is not None:
            self.root.remove()
        else:
            return False

bst = BST()
bst.insert(2442)
bst.insert(23)
bst.insert(123123)
bst.insert(2774)
bst.insert(8123)
bst.insert(1)
bst.insert(723)
bst.inorder()
bst.postorder()
bst.preorder()
