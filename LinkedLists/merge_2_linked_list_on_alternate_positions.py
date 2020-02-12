# merging 2 linked list together to alternate positions
# list "a" a -> b -> c -> d -> e
# list "b" 1 -> 2 -> 3
# merged lists, a -> 1 -> b -> 2 -> c -> 3 -> d -> e and None
# merge b with a, 1 -> a -> 2 -> b -> 3 -> c and d -> e

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def get_head(self):
        return self.head

    def set_head(self, node):
        self.head = node

firstList = LinkedList()
firstList.push('e')
firstList.push('d')
firstList.push('c')
firstList.push('b')
firstList.push('a')

secondList = LinkedList()
secondList.push("3")
secondList.push("2")
secondList.push("1")


def merge_second_into_first(first_list, second_list):
    first_list_current = first_list.get_head()
    second_list_current = second_list.get_head()
    while first_list_current is not None and second_list_current is not None:
        if second_list_current is not None:
            first_list_connect = first_list_current.next
            first_list_current.next = second_list_current
            second_list_connect = second_list_current.next
            second_list.set_head(second_list_connect)
            second_list_current.next = first_list_connect
            first_list_current = first_list_connect
            second_list_current = second_list.get_head()

merge_second_into_first(firstList, secondList)
print("first_list")
firstList.print_list()
print("second_list")
secondList.print_list()

# it works both way
# if we merge firts in to second
# with the current test case going to print
# d -> e and 1 -> a -> 2 -> b -> 3 -> c