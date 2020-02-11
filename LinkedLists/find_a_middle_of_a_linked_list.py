# a -> b -> c -> d -> e -> f
# Find the middle of the linked list, if the linked list is has even number of elements the middle is count / 2 + 1, (the second element in the middle)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f


# the technic that we are going to use
# initiate 2 pointers at the head, fast and slow
# slow steps 1 and fast steps 2
# if fast reach the end take the slow node -> that suppose to be the middle
def find_the_middle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.data


middle = find_the_middle(a)
print("suppose to print 'd' in our case")
print(middle)

e.next = None
middle2 = find_the_middle(a)
print("suppose to print 'c' in our case")
print(middle2)
