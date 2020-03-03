# given a sorted array with integer elements, write an algorithm to create a BST with the minimum height

# first take
# its seems like a balanced BST - we have to find the middle elements
# and it turns out we have to find the middle elements recursively to the left and the right side

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data)
        if self.right is not None:
            self.right.inorder()

    def preorder(self):
        print(f"data {self.data}")
        if self.left is not None:
            print("left-side")
            self.left.preorder()
        if self.right is not None:
            print("right-side")
            self.right.preorder()

def insertFromArray(arr):
    if arr is None or len(arr) == 0:
        return None
    else:
        middle = len(arr) // 2
        root = Node(arr[middle])
        root.left = insertFromArray(arr[:middle])
        root.right = insertFromArray(arr[middle + 1:])
        return root


arrToUse = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bst = insertFromArray(arrToUse)
bst.preorder()
