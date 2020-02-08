# Implementing a Linked List data structure


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        new_node = Node(val)
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def remove(self, val):
        # removing item 2
        # [1 -> 2 -> 3]
        # [1 -> 3]
        if self.head is None:
            return False

        current_node = self.head
        previous_node = None
        removed = False
        while current_node is not None and removed is False:
            if current_node.data is val:
                if previous_node is None:
                    # it means we are at the first iteration
                    # and just need to change the head pointer
                    self.head = current_node.next
                else:
                    # if the element is in the middle of the list
                    # change the next pointer of the previous node
                    previous_node.next = current_node.next
                removed = True
            previous_node = current_node
            current_node = current_node.next
        return removed

    def search(self, val):
        current_node = self.head
        found = False
        while current_node is not None and not found:
            if current_node.data is val:
                found = True
            else:
                current_node = current_node.next
        return found

    def print_values(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


new_list = LinkedList()
for test_val in range(5):
    new_list.add(test_val)

# new_list.print_values()
# print(new_list.search(2))
# print(new_list.search("string"))

value_to_add_and_remove = "this is the value"
new_list.add(value_to_add_and_remove)
new_list.print_values()
new_list.search(value_to_add_and_remove)
print(new_list.remove(value_to_add_and_remove))
print(new_list.search(value_to_add_and_remove))
new_list.remove(2)
print("remove 2")
new_list.print_values()