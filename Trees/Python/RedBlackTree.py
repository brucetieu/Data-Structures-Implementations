# Left Leaning Red Black Tree - 1-1 Correspondence with a 2-3 Tree.

class RedBlackTree:

    class Node:
        def __init__(self, val, count, color):
            self.val = val
            self.left = None
            self.right = None
            self.count = count
            self.color = color

    def __init__(self):
        self.RED = True
        self.BLACK = False
        self.root = None


    def is_red(self, node):
        
        # Leaf nodes are black.
        if node is None:
            return False
        return node.color

    def rotate_left(self, node):
        x = node.right
        x.right = node.left
        x.left = node
        x.color = node.color
        node.color = self.RED
        return x

    def rotate_right(self, node):
        x = node.left
        x.left = node.right
        x.right = node
        x.color = node.color
        node.color = self.RED
        return x
        
    def flip_colors(self, node):
        node.color = self.RED
        node.left.color = self.BLACK
        node.right.color = self.BLACK

