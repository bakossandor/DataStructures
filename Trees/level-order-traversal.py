from collections import deque

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

    def level_order(self):
        queue = deque()
        queue.appendleft(self)
        while len(queue) > 0:
            popped = queue.pop()
            print(popped.data)
            if popped.left is not None:
                queue.appendleft(popped.left)
            if popped.right is not None:
                queue.appendleft(popped.right)



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
bst.level_order()
