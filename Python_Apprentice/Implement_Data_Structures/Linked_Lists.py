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
