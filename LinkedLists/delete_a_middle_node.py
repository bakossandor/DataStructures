# delete a middle node from a single linked list
# given a node which is not the last and not the first in a single linked list, delete it
# now the trick here is that you have only access to the node

# my approach is that delete the current node data and replace with the next node data, then delete the next node as usual

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d

def delete_a_middle_node(node):
    node.data = node.next.data
    node.next = node.next.next

delete_a_middle_node(b)

def print_list(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

print_list(a)