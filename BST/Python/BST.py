
'''
Define node class
'''
class node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

'''
Recursive BST Approach for Insertion, deletion
'''
class bst:
    def __init__(self):
        self.root = None
        self.size = 0

    def get_size(self):
        return self.size

    # Helper method for insertions
    def _insert(self, curr_node, value):
        if value < curr_node.value:
            if curr_node.left == None:
                curr_node.left = node(value)
            else:
                self._insert(curr_node.left, value)
        elif value >= curr_node.value:
            if curr_node.right == None:
                curr_node.right = node(value)
            else:
                self._insert(curr_node.right, value)

    # Main method for insertions
    def insert(self, value):
        # If root is null, create a new node.
        if self.root == None:
            self.root = node(value)
        # Otherwise, insert the node
        else:
            self._insert(self.root, value)
        self.size += 1


    def _inorder_traversal(self, root):
        if root != None:
            self._inorder_traversal(root.left)
            print(root.value)
            self._inorder_traversal(root.right)

    # Inorder traversal: left -> visit -> right
    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _preorder_traversal(self, root):
        if root != None:
            print(root.value)
            self._preorder_traversal(root.left)
            self._preorder_traversal(root.right)

    # Preorder traversal: visit -> left -> right
    def preorder_traversal(self):
        self._preorder_traversal(self.root)

    def _postorder_traversal(self, root):
        if root != None:
            self._postorder_traversal(root.left)
            self._postorder_traversal(root.right)
            print(root.value)

    # Post order traversal: left -> right -> visit
    def postorder_traversal(self):
        self._postorder_traversal(self.root)

    
    # Find minimum value in a tree.
    def find_min(self, root):
        curr = root
        if curr == None:
            return curr
        else:
            while (curr.left != None):
                curr = curr.left
            return curr


    # Find maximum value in a tree.
    def find_max(self, root):
        curr = root
        if curr == None:
            return curr
        else:
            while (curr.right != None):
                curr = curr.right
            return curr

    # Delete a node in the BST.
    def _delete_node(self, root, value):
        prev = None
        curr = root

        # # If BST is empty, return None.
        # if curr == None:
        #     return None

        while curr != None:
            # if curr != None:
            #     prev = curr
            if curr.value == value:
                break
            if value < curr.value:
                # prev = curr
                curr = curr.left
            elif value >= curr.value:
                # prev = curr
                curr = curr.right

        # If node not found, return nothing.
        if curr == None:
            print(value, "is not found.")
            return None
        

        # Traverse BST until desired node is located.
        # if value < curr.value:
        #     while curr.left != None:
        #         prev = curr
        #         curr = curr.left

        #         if value == curr.value:
        #             break
            
            # if value != curr.value:
            #     print(value, "not found")
            #     return

        # elif value >= curr.value:
        #     while curr.right != None:
        #         prev = curr
        #         curr = curr.right
                
        #         if value == curr.value:
        #             break

            # if value != curr.value:
            #     print(value, "not found")
            #     return
        
    

        # Leaf node
        if curr.left == None and curr.right == None:
            # If previous's left is pointing to the current node, delete that link.
            if prev.left == curr:
                prev.left = None
            else:
                prev.right = None

        # Delete one child with a right subtree.
        elif curr.left == None:
            prev.right = curr.right
        
        # Delete one child with a left subtree.
        elif curr.right == None:
            prev.left = curr.left

        # Two children
        else:
            temp_prev = curr
            val = temp_prev.value
            temp = curr.right

            while temp.left != None:
                temp_prev = temp
                temp = temp.left
            
            curr.value = temp.value

            print(val, temp.value)
            if val >= temp.value:
                temp_prev.left = None
            else:
                temp_prev.right = None




            
            

    def delete_node(self, value):
        self._delete_node(self.root, value)

bst = bst()
# bst.insert(4)
# bst.insert(2)
# bst.insert(7)
# bst.insert(1)
# bst.insert(9)
# bst.insert(6)
bst.insert(5)
bst.insert(2)
bst.insert(15)
bst.insert(-4)
bst.insert(4)
bst.insert(9)
bst.insert(21)
bst.insert(19)
bst.insert(25)

bst.delete_node(26)
# bst.delete_node(15)
# bst.delete_node(21)
# bst.delete_node(1)
# bst.delete_node(2)
# bst.delete_node(7)
# bst.delete_node(6)
# bst.delete_node(9)
# bst.delete_node(1)

bst.inorder_traversal()




