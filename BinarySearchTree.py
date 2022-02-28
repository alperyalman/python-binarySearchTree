# Node class is used to define nodes on binary search tree
class Node:
    """
    Node class is used to define nodes on binary search tree
    BinarySearchTree.py
    
    """
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# Binary Search Tree class
class BST:
    # Constructor
    def __init__(self):
        self.root = None

    # Create new node
    def createNode(self,value):
        """Crete node functions"""
        newNode = Node(value)
        # Check if the root node exists
        if (self.root is None):
            self.root = newNode
            return self
        else:
            self.insertNode(self.root, newNode) # Insert node function
        return self

    # Insert node to the left or right to the current node
    def insertNode(self, currentNode, node):
        if (node.value < currentNode.value): # Check if the new node value is less than the current node value 
            if (currentNode.left == None): # If the left node of the current node is null, insert the new node left to the current node
                currentNode.left = node
            else:
                self.insertNode(currentNode.left, node) # If the left node is not null, call the insert function recursively
        else: # If the new node value is bigger than the current node value 
            if (currentNode.right == None): # If the right node of the current node is null, insert the new node right to the current node
                currentNode.right = node
            else:
                self.insertNode(currentNode.right, node) # If the riht node is not null, call the insert function recursively

    # Reference for the followin display functions:
    # https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def _display_aux(self, root):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if root.right is None and root.left is None:
            line = '%s' % root.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if root.right is None:
            lines, n, p, x = self._display_aux(root.left)
            s = '%s' % root.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if root.left is None:
            lines, n, p, x = self._display_aux(root.right)
            s = '%s' % root.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(root.left)
        right, m, q, y = self._display_aux(root.right)
        s = '%s' % root.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def display(self):
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)

    
