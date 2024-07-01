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

    def get_tree_depth(self):
        tree_depth = 1
        if self.left:
            tree_depth += 1

        elif self.right:
            tree_depth += 1
        
        return tree_depth
    
def insert_node(head, node):
    
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

print(head.get_tree_depth())
display_tree(head)