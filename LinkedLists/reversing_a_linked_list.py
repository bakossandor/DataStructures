class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d


def traverse(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next


# check if its working
traverse(a)


def reverse(head):
    current = head
    prev = None
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


reversed_list = reverse(a)
print("--")
traverse(reversed_list)
