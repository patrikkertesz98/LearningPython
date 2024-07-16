class Node:
    def __init__(self, data):
        self.left = None
        self.right = None

        self.data = data

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def get_value(self):
        return self.data

    def set_left_child(self, left_data):
        self.left = left_data

    def set_right_child(self, right_data):
        self.right = right_data

    def set_value(self, data):
        self.data = data

def get_tree_depth(head):
    if head is None:
        return 0

    left_depth=get_tree_depth(head.left)
    right_depth=get_tree_depth(head.right)

    return max(left_depth, right_depth)+1
    
def insert_node(head, node):
    
    if head == node:
        raise Exception("This element is already in the tree")

    if head == None:
        return node
    
    if node.get_value() <= head.get_value():
        head.set_left_child(insert_node(head.get_left_child(), node))
    else:
        head.set_right_child(insert_node(head.get_right_child(), node))

    return head

def display_tree(root, space=0, level_gap=6):
    if root is None:
        return

    # Increase distance between levels
    space += level_gap

    # Process right child first
    display_tree(root.right, space)

    # Print current node after space
    print()
    for i in range(level_gap, space):
        print(end=" ")
    print(root.data)

    # Process left child
    display_tree(root.left, space)


A= Node(45)
B= Node(2)
C= Node(33)
D= Node(54)
E= Node(25)
F= Node(68)
G= Node(72)
H= Node(81)
I= Node(23)


head = insert_node(None, E)

insert_node(head, B)

insert_node(head, C)

insert_node(head, I)

insert_node(head, A)

insert_node(head, H)

insert_node(head, G)

insert_node(head, F)

insert_node(head, Node(89))

print(get_tree_depth(head))
display_tree(head)

def lookup(head, data):

    if head == None:
        return print("Value not found!")
    if head.get_value() == data:
        return head
    if data < head.get_value():
        return lookup(head.get_left_child(), data)
    if data > head.get_value():
        return lookup(head.get_right_child(), data) 
    
def print_node(node):
    if (node == None):
        print("Node not found.")
    
    print(node.get_value())

def min_value(head):
    current = head

    while(current.left != None):
        current = current.left

    return current.data

def max_value(head):
    current = head

    while(current.right != None):
        current = current.right

    return current.data

print("Looking up 45: ", end="")
print_node(lookup(head, 45))

print("Minimum value:", min_value(head))
print("Maximum value:", max_value(head))

class MyQueue:

    def __init__(self):

        """ Create a new queue. """
        self.items = []
    
    def is_empty(self):
        
        """Returns true if the queue is empty."""

        return len(self.items) == 0
    
    def enqueue(self, item):

        """ Add item to queue"""

        self.items.append(item)

    def dequeue(self):

        """ Removes the top element from the queue. """

        return self.items.pop(0)
    
    def size(self):

        """ Return the size of the queue """
        return len(self.items)
    
    def peek(self):

        """ Show the top element. """

        if self.is_empty:
            raise Exception("Nothing to peek.")
        
        return self.items[0]
    
def breadth_first(node):

    if (node == None):
        raise Exception("No root found")
    
    path = []

    queue = MyQueue()
    queue.enqueue(node)

    while queue.size() > 0:
        current = queue.dequeue()

        path.append(current.data)

        if current.get_left_child() != None:
            queue.enqueue(current.get_left_child())
        
        if current.get_right_child() != None:
            queue.enqueue(current.get_right_child())
    
    return path

print(breadth_first(head))