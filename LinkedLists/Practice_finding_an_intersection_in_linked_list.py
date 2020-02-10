# finding an intersection in a linked list
# a -> b -> c -> d -> e -> f
# 1 -> 2 -> 3 -> e

# first we have to take how many steps it take to traverse the the two lists
# we take the difference - start stepping from the longest list with the difference - after we stepp together - if the nodes met along the road the 2 list have an intersection otherwise not

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

one = Node(1)
two = Node(2)
three = Node(3)
one.next = two
two.next = three
three.next = e

# the 2 linked list heads are "a" and "one"
# we assume the 2 lists has an intersection and not looped

def find_the_intersection(head1, head2):
    count1 = 0
    current1 = head1
    while current1 is not None:
        count1 += 1
        current1 = current1.next
    count2 = 0
    current2 = head2
    while current2 is not None:
        count2 += 1
        current2 = current2.next
    pointer1 = head1
    pointer2 = head2
    if count1 >= count2:
        diff = count1 - count2
        while diff != 0:
            pointer1 = pointer1.next
            diff -= 1
    else:
        diff = count2 - count1
        while diff != 0:
            pointer2 = pointer2.next
            diff -= 1
    while pointer1 is not None and pointer2 is not None:
        if pointer1 == pointer2:
            print(f"intersection data: {pointer1.data}")
            return
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    print("there is no intersection")



find_the_intersection(a, one)
# -> it prints e

# modify the list to detect there is no intersection
three.next = None
print("\nNow supposed to be no intersection: -->")
find_the_intersection(a, one)