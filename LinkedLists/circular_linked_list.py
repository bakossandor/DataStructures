class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.tail.next = self.head

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
        self.tail = new_node

    def remove(self, val):
        if val is self.head:
            self.head = self.head.next
            self.tail.next = self.head
            return True
        else:
            current = self.head
            previous = None
            while current:
                if val is current.data:
                    previous.next = current.next
                    return True
                previous = current
                current = current.next
                if current is self.head:
                    break
            return False

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            if current is self.head:
                break


cllist = CircularLinkedList()
# cllist.prepend("a")
# cllist.prepend("b")
# cllist.prepend("c")
cllist.append("1")
cllist.append("5")
cllist.append("9")
# cllist.prepend("b")
# cllist.prepend("c")
print(cllist.remove("5"))
cllist.prepend("4234")
cllist.append("what")

cllist.print()
