class Node:

    def __init__(self, dataval=None, nextval=None):
        '''
        A node in a singly-linked list.
        '''
        self.dataval = dataval
        self.nextval = nextval

    def __repr__(self):
        return repr(self.dataval)

class LinkedList:

    def __init__(self):
        '''
        Creating a new singly-linked list.
        '''
        self.head = None

    def __repr__(self):
        '''
        Creating a string represantation of the data in a list.
        '''
        nodes = []
        curr = self.head

        while curr:
            nodes.append(repr(curr))
            curr = curr.nextval

        return '[' + '->'.join(nodes) + ']'

    def prepend(self, dataval):

        '''
        Insert a new element at the beginning of the list.
        '''

        self.head = Node(dataval=dataval, nextval=self.head)

    def append(self, dataval):
        '''
        Insert a new element at the end of the list.
        '''

        if not self.head:
            self.head = Node(dataval=dataval)
            return

        curr = self.head

        while curr.nextval:
            curr = curr.nextval
        
        curr.nextval = Node(dataval = dataval)

    def add_after(self, middle_dataval, dataval):
        """
        Insert a new element after the node with middle_dataval.
        """

        if middle_dataval is None:
            print("Data to insert after not specified.")
            return
        
        curr = self.head

        while curr and curr.dataval != middle_dataval:
            curr = curr.nextval

        new_node = Node(dataval=dataval)

        new_node.nextval = curr.nextval
        curr.nextval = new_node

    def find(self, data):
        """
        Search for the first element that matches the data paramenter.
        """

        curr = self.head

        while curr and curr.dataval != data:
            curr = curr.nextval

        return curr
    
    def remove(self, data):
        """
        Remove an element.
        """
        curr = self.head
        prev = None

        while curr and curr.dataval != data:
            prev = curr
            curr = curr.nextval

        if prev is None:
            self.head = curr.nextval
        elif curr:
            prev.nextval = curr.nextval
            curr.nextval = None

    def reverse(self):

        """ Reverse the list in-place. """
        curr = self.head

        prev_node = None
        next_node = None

        while curr:
            next_node = curr.nextval
            curr.nextval = prev_node

            prev_node = curr

            curr = next_node

        self.head = prev_node

    def reverse_in_recursive(self):

        """ 
        Recursive reverse function.
        """

        def recursion(curr, prev_node):
            if not curr:
                return prev_node
            
            next_node = curr.nextval
            curr.nextval = prev_node

            prev_node = curr

            curr = next_node

            return recursion(curr, prev_node)
        
        self.head = recursion(curr=self.head, prev_node=None)
        

    def count_node(self):
        """
        Count the number of nodes in the linked list.
        """

        if (self.head == None):
            return 0
        else:
            curr = self.head
            count = 0
            while (curr != None):
                curr = curr.nextval
                count += 1
        return count
    

numbers = LinkedList()

print(numbers)

numbers.append("two")
numbers.append("three")

print(numbers)

numbers.prepend("one")
numbers.prepend("zero")

print(numbers)

numbers.append("four")
numbers.append("six")

print(numbers)

numbers.add_after("four", "five")

print(numbers)

numbers.reverse()

print(numbers)

numbers.reverse_in_recursive()

print(numbers)

numbers.remove("one")

print(numbers)

numbers.remove("six")

print(numbers)

print(numbers.count_node())



