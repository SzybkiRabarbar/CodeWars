class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes

def tree_to_list(tree_root):
    pass

print(Node(1, [Node(2, [Node(3), Node(4), Node(5)]), Node(3, [Node(7)])]), [1, 2, 3, 3, 4, 5, 7])