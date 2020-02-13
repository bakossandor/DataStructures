# Given a linked list where every node represents a linked list and contains two pointers of its type:
# (i) Pointer to next node in the main list (we call it ‘right’ pointer in below code)
# (ii) Pointer to a linked list where this node is head (we call it ‘down’ pointer in below code).
# All linked lists are sorted. See the following example
# 5 -> 10 -> 19 -> 28
# |    |     |     |
# ˇ    ˇ     ˇ     ˇ
# 7    20    22    35
# |          |     |
# ˇ          ˇ     ˇ
# 8          50    40
# |                |
# ˇ                ˇ
# 30               45
#
# Write a function flatten() to flatten the lists into a single linked list. The flattened linked list should also be sorted
# for example, for the above input list, output list should be 5->7->8->10->19->20->22->28->30->35->40->45->50.

# creating the different lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.sublist_next = None


five = Node(5)
ten = Node(10)
nineteen = Node(19)
twentyeight = Node(28)
five.next = ten
ten.next = nineteen
nineteen.next = twentyeight

seven = Node(7)
eight = Node(8)
thirty = Node(30)

five.sublist_next = seven
seven.sublist_next = eight
eight.sublist_next = thirty

twenty = Node(20)
ten.sublist_next = twenty

twentytwo = Node(22)
fifty = Node(50)
nineteen.sublist_next = twentytwo
twentytwo.sublist_next = fifty

thirtyfive = Node(35)
forty = Node(40)
fortyfive = Node(45)
twentyeight.sublist_next = thirtyfive
thirtyfive.sublist_next = forty
forty.sublist_next = fortyfive

# with this exercise we don't have to worry about the head change
def flatten(head):
    current_on_the_main = head
    while current_on_the_main is not None:
        while current_on_the_main.sublist_next is not None:
            merge_place = current_on_the_main.next
            while True:
                if merge_place is None or (merge_place.data > current_on_the_main.sublist_next.data):
                    # then merge it
                    current_on_the_main.sublist_next.next = merge_place
                    current_on_the_main.next = current_on_the_main.sublist_next
                    temp = current_on_the_main.sublist_next
                    current_on_the_main.sublist_next = current_on_the_main.sublist_next.sublist_next
                    temp.sublist_next = None
                    break
                merge_place = merge_place.next
        current_on_the_main = current_on_the_main.next






def print_list(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next


flatten(five)
print_list(five)