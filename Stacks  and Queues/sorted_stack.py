# write a stack which sorts it's elements like the smallest number is in the top of the stack
# you can use an another stack, but no other data structure to copy and store elements from the original stack ds

# my first approach would be, to copy back and forth the numbers from the stack, and insert the new element into the right place

class sorted_stack:
    def __init__(self):
        self.stack_sorted = []

    def add(self, num):
        if len(self.stack_sorted) == 0:
            self.stack_sorted.append(num)
        else:
            added = False
            stack_helper = []
            while len(self.stack_sorted) != 0:
                top = self.stack_sorted.pop()
                if added is True:
                    stack_helper.append(top)
                else:
                    if top < num:
                        stack_helper.append(top)
                        continue
                    elif top >= num:
                        stack_helper.append(num)
                        stack_helper.append(top)
                    added = True
            if added is False:
                stack_helper.append(num)
            while len(stack_helper) != 0:
                self.stack_sorted.append(stack_helper.pop())

    def print_stack(self):
        print(self.stack_sorted)


stack1 = sorted_stack()
stack1.add(4)
stack1.add(2323)
stack1.add(3525626)
stack1.add(2)
stack1.add(-2)
stack1.add(0)
stack1.add(55)
stack1.print_stack()