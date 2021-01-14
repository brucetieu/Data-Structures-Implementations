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