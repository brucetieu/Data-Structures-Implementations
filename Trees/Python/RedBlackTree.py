from queue import Queue


# Left Leaning Red Black Tree - 1-1 Correspondence with a 2-3 Tree.

class RedBlackTree:

    class Node:
        def __init__(self, val, color):
            self.val = val
            self.left = None
            self.right = None
            self.color = color

    def __init__(self):
        self.RED = True
        self.BLACK = False
        self.root = None
        self.queue = Queue(maxsize=100)


    def is_red(self, node):
        
        # Leaf nodes are black.
        if node is None:
            return False
        return node.color

    def rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = self.RED
        return x

    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = self.RED
        return x
        
    def flip_colors(self, node):
        node.color = self.RED
        node.left.color = self.BLACK
        node.right.color = self.BLACK

    def insert(self, val):
        self.root = self._insert(self.root, val)
        
        # Make sure root of tree is always black.
        self.root.color = self.BLACK

    def _insert(self, node, val):

        # Insert a leaf node, with the link of the parent being colored red.
        if node is None:
            node = self.Node(val, self.RED)

        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(root.right, val)
        else:
            node.val = val # Replace value, avoid duplicates

        # Perform rotations if necessary.
        if not self.is_red(node.left) and self.is_red(node.right):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        return node
        
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if root is not None:
            self._inorder(root.left)
            print(root.val)
            self._inorder(root.right)

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, root):
        if root is not None:
            print(root.val)
            self._preorder(root.left)
            self._preorder(root.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, root):
        if root is not None:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.val)


    def level_order(self):
        '''Breadth first traversal of BST.'''
        self.queue.put(self.root)

        while not self.queue.empty():
            node = self.queue.get() # dequeue
            print(node.val)
            
            if node.left is not None:
                self.queue.put(node.left)
            if node.right is not None:
                self.queue.put(node.right)

    def search(self, val):

        curr = self.root
        
        while curr is not None:
            if val > curr.val:
                curr = curr.right
            elif val < curr.val:
                curr = curr.left
            else:
                return True
        
        return False

    # TODO: add delete_min / delete_max and delete methods

my_red_black_tree = RedBlackTree()

my_red_black_tree.insert('S')
my_red_black_tree.insert('E')
my_red_black_tree.insert('A')

my_red_black_tree.level_order()

