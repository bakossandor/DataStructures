# you have 2 number represented by 2 linked list
# 1 -> 2 -> 3 = 321 and 4 -> 5 -> 6 = 654
# sum the two number together and return a summed linked list
# questions might be asked? is it ok if I modify, mutate the original list?
# so we might need to access a node class as well if we want to append a new node when the sums exceeds 9 and turns into 2 digit


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createLinkedList(values):
    head = None
    prev = None
    for idx, value in enumerate(values):
        new_node = Node(value)
        if idx == 0:
            head = new_node
            prev = head
        else:
            prev.next = new_node
            prev = new_node
    return head


def print_list(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next


LL1 = createLinkedList([1, 2, 3])
LL2 = createLinkedList([4, 5, 8])


def sum_them_together(list1, list2):
    sums = []
    remainder = 0
    while list1 is not None or list2 is not None:
        num1 = list1.data if list1 is not None else 0
        num2 = list2.data if list2 is not None else 0
        sum_all = num1 + num2 + remainder
        if sum_all >= 10:
            remainder = 1
            sums.append(sum_all - 10)
        else:
            remainder = 0
            sums.append(sum_all)
        list1 = list1.next
        list2 = list2.next
    if remainder == 1:
        sums.append(1)
    return createLinkedList(sums)


new_list_head = sum_them_together(LL1, LL2)
print_list(new_list_head)
# new list suppose to be 5->7->1->1