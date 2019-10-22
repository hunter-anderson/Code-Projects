#crude implementation of a stack
#10/17/2019 - Hunter Anderson

class Stack:
    def __init__(self):
        self._array = []
        self._top = -1

    #inserts element at top of stack, return True if successful
    def push(self, element):
        self._array.append(element)
        self._top += 1
        if self._array[self._top] == element:
            return True
        return False

    #Return -> top element of stack
    #raise error if stack is empty
    def top(self):
        if self._top != -1:
            return self._array[self._top]
        else:
            raise Exception("Error: stack is empty")

    #removes last element on stack and returns it
    #Return -> top of stack
    def pop(self):
        top = self.top()
        self._array = self._array[:-1]
        self._top -= 1
        return top

    #returns whether the stack is empty or not
    #Return -> bool
    def isEmpty(self):
        return True if self._top is -1 else False
