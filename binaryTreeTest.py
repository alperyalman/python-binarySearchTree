from BinarySearchTree import *

# Create new binary search tree
bst = BST() 
node_values = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]

# Add node values to binary search tree, first value will be the root
for val in node_values:
    bst.createNode(val)

# Display binary search tree
bst.display()

searching_node, info = bst.find(65)
print(info)

