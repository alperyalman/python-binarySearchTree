# Python - Binary Search Tree

    # Scripts
    BinarySearchTree.py ->  Inludes classes and function to create binary 
                            search tree, add, display and find nodes

    binaryTreeTest.py   ->  Test sctipt

    # Classes defined in BinarySearchTree.py
    class Node  ->  The class that is used to create Node structure     
    class BST   ->  The class used to create Binary Search Tree, 
                    insert and find nodes
    
    # Functions in BST class
    BST.createNode(value)   ->  creeateNode function is used to create node on 
                                the tree 
    BST.def find(val)       ->  find function is used to find the node      
                                corresponding given node value

    BST.display()           ->  display function visually shows the binary 
                                search tree 


## Example 
Node values will be [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]. 

* 7 is the root node
* 5 is added left to 7
* 1 is added left to 5
* 8 is added right to 7
* 3 is added right to 1
* 6 is added right to 5
* 0 is added left to 1
* 9 is added right to 8
* 4 is added right to 3
* 2 is added left to 3

___Test script:___

```python
from BinarySearchTree import *

# Create new binary search tree
bst = BST() 
node_values = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]

# Add node values to binary search tree, first value will be the root
for val in node_values:
    bst.createNode(val)

# Display binary search tree
bst.display()

# Find node
searching_node, info = bst.find(0)
print(info)
```

___Output:___ 

           _7
          /  \
      ___5   8
     /    \   \
    1_    6   9
     / \
    0   3
       / \
       2  4

