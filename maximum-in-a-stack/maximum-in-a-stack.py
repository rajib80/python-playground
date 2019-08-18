# Implement a class for a stack that supports all the regular functions 
# (push, pop) and an additional function of max() which returns 
# the maximum element in the stack (return None if the stack is empty). 
# Each method should run in constant time.

class Stack:
    def __init__(self):
        self.stack = list()
        self.track = list()
    
    def push(self, value):
        if len(self.stack) <= 0:
            self.stack.append(value)
            self.track.append(value)
        else:
            current_max = self.track[len(self.track) - 1]
            if current_max < value:
                self.track.append(value)
            else:
                self.track.append(current_max)
            self.stack.append(value)
    
    def pop(self):
        if len(self.stack) <= 0:
            return None
        self.track.pop()
        return self.stack.pop()
    
    def max(self):
        if len(self.stack) <= 0:
            return None
        return self.track[len(self.track) - 1]


# Test code
myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(2)

print(myStack.max())
# 3
myStack.pop()
myStack.pop()
print(myStack.max())
# 2



