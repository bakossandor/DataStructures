# practice implementing and using linked lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Write a code to remove duplicaties from an unsorted linked list
# input "a" -> "b" -> "c" -> "a" -> "b" -> "d"
# output "a" -> "b" -> "c" -> "d"


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


# creating the linked list
# node values
values = ["a", "b", "c", "a", "b", "d"]
LLH = createLinkedList(values)
def print_list(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next


# so we have the linked list with duplicates
# my initial thought is to have a directory to access elements in near constant time like a dictionary or hash table to store the different values
# moving one by one and storing the elements in the dictionary, if an element already exist, remove the current from the list and move forward
def remove_duplicates(head):
    dictionary = {}
    current = head
    previous = None
    while current is not None:
        if dictionary.get(current.data) is True:
            # then remove the node
            previous.next = current.next
            current = previous
        else:
            dictionary[current.data] = True
        previous = current
        current = current.next
    return head

# print_list(remove_duplicates(LLH))
# it should print out "a" -> "b" -> "c" -> "d"


###
# removing duplicates without using a dictionary
def remove_duplicates_without_dict(head):
    current = head
    while current is not None:
        sub_current = current.next
        sub_previous = current
        while sub_current is not None:
            if sub_current.data == current.data:
                sub_previous.next = sub_current.next
                sub_current = sub_previous
            sub_previous = sub_current
            sub_current = sub_current.next
        current = current.next
    return head

# print_list(remove_duplicates_without_dict(LLH))
# it should print out "a" -> "b" -> "c" -> "d"


### second question
# implement an algorithm which finds the kth element to the last
# the obvius solution is that count the element and start from the beginning, or if the size of the list known move (size - Kth element)
# But there is a recursive solution as well
# The recursive approach would be to recurse until the end, and from the end start to count, if the counter is the number we want, return the data to the top

def return_k_last(head_node, k_minus):
    if head_node.next is not None:
        current = return_k_last(head_node.next, k_minus)
        if isinstance(current, Node):
            return current
        if current == k_minus:
            return head_node
        else:
            return current + 1
    else:
        return 1

# return_node = return_k_last(LLH, 1)
# print(return_node.data)



