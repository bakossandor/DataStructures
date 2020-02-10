class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# creating a linked list with a loop
# a -> b -> c -> d -> b
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
d.next = b

# Detect a loop in a linked list and remove it
# technic we use:
# 1. detect the loop with the floyd's method - with a slow and faster steps in the list
# if we have the loop - count how many elements the loop has
# set 2 pointer to the head
# move 1 by the number of the elements in the loop
# then move them together where they met there is the loop - and we need to untangle that previous element
# so in this example they met in "b"

def untangle(head, a_node_in_the_loop):
    count = 0
    current = a_node_in_the_loop
    while True:
        count += 1
        current = current.next
        if current is a_node_in_the_loop:
            break
    pointer_from_the_beginning = head
    moved_pointer = head
    # count is always at leas 1
    while count != 0:
        moved_pointer = moved_pointer.next
        count -= 1
    while pointer_from_the_beginning.next is not moved_pointer.next:
        moved_pointer = moved_pointer.next
        pointer_from_the_beginning = pointer_from_the_beginning.next
    print(f"this is the 'cross-road' {pointer_from_the_beginning.next.data}")
    moved_pointer.next = None
    return True


def detect_a_loop(head):
    slow = head
    fast = head.next
    # check if next always point to the next Node
    while slow is not None and fast is not None and fast.next is not None:
        if slow is fast:
            # then we need to untangle
            print("loop detected")
            return untangle(head, slow)
        slow = slow.next
        fast = fast.next.next
    return False


loop = detect_a_loop(a)
print(loop)

# finally just iterate through the linked list
def print_nodes(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next


print_nodes(a)