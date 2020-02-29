# describe how would you implement 3 stack in a single array

# I would divide the array into 3 spaces and use pointer to mark the end of each stack
# [stack1, stack1, stack2, stack2, stack3, stack3]
# [None, None, "1", None, "one", "two"]

class threeStack:
    def __init__(self):
        self.one = 0
        self.two = 0
        self.three = 0
        self.arr = []

    def add(self, data, where):
        if where == 1:
            self.arr.insert(self.one, data)
            self.one += 1
        elif where == 2:
            self.arr.insert(self.one + self.two, data)
            self.two += 1
        elif where == 3:
            self.arr.insert(self.one + self.two + self.three, data)
            self.three += 1

    def printArr(self):
        print(self.arr)


stack = threeStack()
stack.add("whatup", 3)
stack.add("wher is this", 1)
stack.add("twotwo", 2)
stack.add("one one", 1)
stack.printArr()