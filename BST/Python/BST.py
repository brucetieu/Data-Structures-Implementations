
class Node:
    '''Node class'''

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BST:

    '''Initialize root and size variables. Binary Search Tree class'''
    def __init__(self):
        self.root = None
        self.size = 0


    '''Get the number of nodes in the BST.'''
    def get_size(self):
        return self.size


    def _insert(self, curr_node, value):
        '''Helper method for inserting node into a BST.'''

        # Insert node to the left subtree if the value is less than the current nodes.
        if value < curr_node.value:

            # Create a new node if we need to insert a leaf node.
            if curr_node.left == None:
                curr_node.left = Node(value)
            else:
                self._insert(curr_node.left, value)

        # Insert node to the right subtree if the value is less than the current nodes.
        elif value >= curr_node.value:

            # Create a new node if we need to insert a leaf node.
            if curr_node.right == None:
                curr_node.right = Node(value)
            else:
                self._insert(curr_node.right, value)


    def insert(self, value):
        '''Public method for inserting node into the BST'''

        # If root is null, create a new node.
        if self.root == None:
            self.root = Node(value)
        # Otherwise, insert the node
        else:
            self._insert(self.root, value)

        # Increment size of BST by 1.
        self.size += 1


    def _inorder_traversal(self, root):
        ''' Inorder traversal: left -> visit -> right'''
        if root != None:
            self._inorder_traversal(root.left)
            print(root.value)
            self._inorder_traversal(root.right)


    def inorder_traversal(self):
        self._inorder_traversal(self.root)


    def _preorder_traversal(self, root):
        '''Preorder traversal: visit -> left -> right'''
        if root != None:
            print(root.value)
            self._preorder_traversal(root.left)
            self._preorder_traversal(root.right)


    def preorder_traversal(self):
        self._preorder_traversal(self.root)

    def _postorder_traversal(self, root):
        '''Post order traversal: left -> right -> visit'''
        if root != None:
            self._postorder_traversal(root.left)
            self._postorder_traversal(root.right)
            print(root.value)


    def postorder_traversal(self):
        self._postorder_traversal(self.root)


    def _find_min(self, root):
        curr = root
        if curr == None:
            return None
        else:
            while (curr.left != None):
                curr = curr.left
            return curr.value


    def _find_max(self, root):
        curr = root
        if curr == None:
            return None
        else:
            while (curr.right != None):
                curr = curr.right

            return curr.value


    def find_min(self):
        min = self._find_min(self.root)
        return min


    def find_max(self):
        max = self._find_max(self.root)
        return max

    '''
    Helper method for deleting a node in a BST - Iterative approach.
    '''

    def _delete_node_iterative(self, root, value):

        # Keep track of the previous node to update pointers accordingly.
        prev = None

        # Keep track of the current node.
        curr = root

        # Traverse through the BST until we locate the node to be deleted.
        while curr != None:

            # The node has been located for deletion.
            if curr.value == value:
                break

            if value < curr.value:
                prev = curr
                curr = curr.left
            elif value >= curr.value:
                prev = curr
                curr = curr.right

        # If node not found, return nothing.
        if curr == None:
            print(value, "is not found.")
            return None

        # Delete a leaf node.
        if curr.left == None and curr.right == None:

            # If the node to be deleted is root, and it has no children, delete it.
            if prev == None:
                self.root = None
                return self.root

            # If previous's left is pointing to the current node, delete that link.
            if prev.left == curr:
                prev.left = None
            else:
                prev.right = None

        # Delete a child node with a right subtree.
        elif curr.left == None:

            # If the node to be deleted is a root, and it has one child, just set the next node to be the root.
            if prev == None:
                self.root = self.root.right

            elif prev.left == curr:
                prev.left = curr.right
            elif prev.right == curr:
                prev.right = curr.right

        # Delete a child node with a left subtree.
        elif curr.right == None:

            # If the node to be deleted is a root, and it has one child, just set the next node to be the root.
            if prev == None:
                self.root = self.root.left

            # Set the previous pointer to point to the node after the one that is deleted.
            elif prev.left == curr:
                prev.left = curr.left

            elif prev.right == curr:
                prev.right = curr.left

        # Delete a node which contains two children.
        else:

            # Keep track of the node before the node containing the minimum.
            temp_prev = curr

            # Use this temp node to traverse the right subtree.
            temp = curr.right

            # Traverse the right subtree until we've found the node with the minimum value.
            while temp.left != None:
                temp_prev = temp
                temp = temp.left

            # We've located the minimum value in the right subtree. So replace the curr node's value with this minium value.
            curr.value = temp.value

            # Then, delete the node containing the mininum value.
            if temp_prev.left == temp:
                temp_prev.left = None

            elif temp_prev.right == temp:
                temp_prev.right = None


    def delete_node_iterative(self, value):
        self._delete_node_iterative(self.root, value)


    def _find_node(self, root, value):
        '''Find a node in the BST'''

        if root == None:
            return root

        if value < root.value:
            self._find_node(root.left, value)
        elif value > root.value:
            self._find_node(root.right, value)

        else:
            return 1

        return -1



    def find_node(self, value):
        return self._find_node(self.root, value)


    def delete_node_recursive(self, value):
        self._delete_node_recursive(self.root, value)


    def _inorder_predecessor(self, root):
        while root.right != None:
            root = root.right
        return root.val


    def _inorder_successor(self, root):
        while root.left != None:
            root = root.left
        return root.val


    def _delete_node_recursive(self, root, value):
        if root is None:
            return root

        if value > root.value:
            root.right = self._delete_node_recursive(root.right, value)
        elif value < root.value:
            root.left = self._delete_node_recursive(root.left, value)

        # The value is found.
        else:

            # Leaf node -> the base case.
            if root.left is None and root.right is None:
                root = None

            # One or two children.
            elif root.left:
                root.value = self._inorder_predecessor(root.left)
                root.left = self._delete_node_recursive(root.left, root.value)
            else:
                root.value = self._inorder_successor(root.right)
                root.right = self._delete_node_recursive(root.right, root.value)

        return root


bst = BST()

bst.insert(5)
bst.insert(2)
bst.insert(15)
bst.insert(-4)
bst.insert(4)
bst.insert(9)
bst.insert(21)
bst.insert(19)
bst.insert(25)

bst.delete_node_recursive(25)

print(bst.find_node(6))

bst.inorder_traversal()
print()
bst.postorder_traversal()
print()
bst.preorder_traversal()

print("max", bst.find_max())
print("min", bst.find_min())
