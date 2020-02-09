class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def print_out(self):
        current = self.head
        while current.data is not None:
            print(current.data)
            if current.next is self.head:
                break
            current = current.next

    def return_head(self):
        return self.head


cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)

print("The circular linked list is the following:")
cll.print_out()
print("\n")

# detect the loop
# head of the ccl
head = cll.return_head()


def detect_the_loop(head_of_the_list):
    step1 = head_of_the_list
    step2 = head_of_the_list.next
    while step1.next is not None and step2.next is not None and step2.next.next:
        if step1 is step2:
            return True
        step1 = step1.next
        step2 = step2.next.next
    return False


loop = detect_the_loop(head)
print("is circular")
print(loop)

# creating a list like that
# a -> b -> c -> d
#           ^    |
#           |    ˇ
#           f <- e

# creating a linked list
# a -> b -> c -> d
a = Node("a")
b = Node("b")
a.next = b
c = Node("c")
b.next = c
d = Node("d")
c.next = d


# check the identical function with a SingleLinkedList
no_loop = detect_the_loop(a)
print("loop ?")
print(no_loop)

# creating a list like that
# a -> b -> c -> d
#           ^    |
#           |    ˇ
#           f <- e

e = Node("e")
d.next = e
f = Node("e")
e.next = f
f.next = c

loop2 = detect_the_loop(a)
print("loop ?")
print(loop2)
