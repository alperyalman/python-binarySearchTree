from BinarySearchTree import *

# Create new binary search tree -> tree_obj = BST()
bst = BST() 
node_values = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]

# Add node values to binary search tree -> tree_obj.createNode(node_value) 
# First value will be the root
for val in node_values:
    bst.createNode(val)

# Display binary search tree -> tree_obj.display()
bst.display()

# Find node -> tree_obj.find(node_value)
searching_node, info = bst.find(0)
print(info) # Print information about searching node