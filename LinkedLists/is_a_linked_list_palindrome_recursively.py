# find out if the linked list is a palindrome
# so the recursive approach is to go until the middle with each step
# after finding the middle return the next element from the middle and so on and compare them with the first half od the node

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

LL1 = createLinkedList([1, 2, 3, 4, 1])

def find_length(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count

def is_pal_recursive(node, length):
    if length == 1 or length == 0:
        return node.next
    else:
        result = is_pal_recursive(node.next, length - 2)
        if result is False:
            return False
        else:
            compared = result.data == node.data
            if compared is False:
                return False
            return result.next



def is_linked_list_palindrome(head):
    length = find_length(head)
    result = is_pal_recursive(head, length)
    if result is None:
        return True
    elif result is False:
        return False


print(is_linked_list_palindrome(LL1))