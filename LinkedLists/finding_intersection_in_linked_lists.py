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
e = Node("intersection")
d.next = e
f = Node("f")
e.next = f
g = Node("g")
f.next = g
h = Node("h")
g.next = h

a2 = Node("a2")
b2 = Node("b2")

a2.next = b2
b2.next = e


def find_intersection(head1, head2):
    count1 = 0
    count2 = 0
    current1 = head1
    current2 = head2
    while current1 is not None or current2 is not None:
        if current1 is not None:
            count1 += 1
            current1 = current1.next
        if current2 is not None:
            count2 += 1
            current2 = current2.next
    current1 = head1
    current2 = head2
    if count1 > count2:
        diff = count1 - count2
        while diff != 0:
            current1 = current1.next
            diff -= 1
        while current1 is not None and current2 is not None:
            if current1 is current2:
                return current1.data
            current1 = current1.next
            current2 = current2.next
        return False


print(find_intersection(a, a2))



