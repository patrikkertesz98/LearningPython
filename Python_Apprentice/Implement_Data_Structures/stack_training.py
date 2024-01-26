stack = []

stack.append('United States(USA)')
stack.append('Great Britain(GBR)')
stack.append('China(CHN)')

print(stack.pop())

class Stack:

    def __init__(self):
        """ Create a new stack. """
        self.stack = []

    def push(self, data):
        """ Add a element to the stack. """
        self.stack.append(data)

    def pop(self):
        """ Removes element from the top of the stack. """
        if self.is_empty():
            raise Exception("Nothing to pop. (Stack is empty). ")
        return self.stack.pop(len(self.stack)-1)

    def peek(self):
        """ Peeks at an element from the top of the stack. """
        if self.is_empty():
            raise Exception("Nothing to peek. (Stack is empty). ")
        return self.stack[len(self.stack)-1]

    def is_empty(self):
        """ Return true if stack is empty. """
        return self.size() == 0
    
    def size(self):
        """ Return size of the stack. """
        return len(self.stack)

mystack = Stack()
secondmystack = Stack()

print(mystack)
print(secondmystack)

print(mystack.is_empty())

mystack.push("Dóri")

print(mystack.is_empty())