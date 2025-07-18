---
title: Python - Binary Tree - Implementation
tags: studies, programming
use: Documentation
languages: Python
dependences: NULL
---

<details> <summary>Table of Contents 🔖</summary>

- [Code File #](#code-file-)
- [Explanation](#explanation)
- [Found in Programiz](#found-in-programiz)

</details>

---

# Code File [#](binary_tree.py)

The [code](#found-in-programiz) provided seems to be checking whether a binary tree is a full binary tree or not. However, there are a few bugs in the code that need to be addressed:

1.  In the `isFullTree` function, the condition `if root.leftChild is not None and root.rightChild is not None` is incorrect. It should be `if root.leftChild is None and root.rightChild is None`. This condition checks if both the left and right child are absent, indicating a leaf node. In the current code, it checks if both the left and right child are present.
    
2.  The logic to check for a full binary tree is incorrect. In a full binary tree, each node should have either 0 or 2 child nodes. The corrected logic should be:
    
    -   If the root is None, return True (as an empty tree is considered a full binary tree).
    -   If both the left and right child nodes are None, return True.
    -   If either the left child or the right child is None (not both), return False.
    -   Recursively check if both the left and right subtrees are full binary trees using `isFullTree`.


# Explanation

```python
class Node:
    def __init__(self, item):
        self.item = item
        self.leftChild = None
        self.rightChild = None
```

This part of the code defines a special type of object called `Node`. Think of a `Node` as a single element in our tree. Each `Node` has a value (`item`) and can have a left child and a right child. For now, the children are set to `None`.

```python
def isFullTree(root):
    if root is None:
        return True
```

This function, `isFullTree`, checks if a tree is full or not. A tree can be empty, which means it doesn't have any nodes. In that case, we consider it a full tree, so we return `True`.

```python
if root.leftChild is None and root.rightChild is None:
        return True
```

If a `Node` doesn't have any children (both left and right children are `None`), it means it's a leaf node, like the end of a branch. In a full tree, all the nodes should either have no children or have both a left and a right child. So, if a `Node` has no children, we consider it a full tree, and we return `True`.

```python
if root.leftChild is None or root.rightChild is None:
        return False
```

If a `Node` has only one child (either left or right, but not both), it means it's not a full tree. In a full tree, every node should have either no children or two children. So, if a `Node` has only one child, we consider it not a full tree, and we return `False`.

```python
return isFullTree(root.leftChild) and isFullTree(root.rightChild)
```

If the `Node` has both a left and a right child, we need to check if both of those child trees are also full trees. We do this by calling the `isFullTree` function recursively on the left child and the right child of the current `Node`. If both child trees are full trees, we return `True`. Otherwise, we return `False`.

```python
root = Node(1)
root.leftChild = Node(2)
root.rightChild = Node(3)
root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.rightChild.leftChild = Node(6)
root.rightChild.rightChild = Node(7)
```

Here, we create a binary tree by connecting the nodes together. We start with a root node with a value of 1. Then, we create other nodes and connect them as children to form the tree structure. For example, the root node has a left child with a value of 2, and that left child has its own left and right children, and so on.

```python
if isFullTree(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")
```

Finally, we check if the tree we created is a full binary tree by calling the `isFullTree` function with the root node as the argument. If the tree is a full binary tree, we print "The tree is a full binary tree." Otherwise, we print "The tree is not a full binary tree."

# Found in [Programiz](https://www.programiz.com/dsa/full-binary-tree#python-code)

```python
# Checking if a binary tree is a full binary tree in Python

# Creating a node
class Node:
    def __init__(self, item):
        self.item = item
        self.leftChild = None
        self.rightChild = None

# Checking full binary tree
def isFullTree(root):
    # Tree empty case
    if root is None:
        return True

    # Checking whether child is present
    if root.leftChild is None and root.rightChild is None:
        return True

    if root.leftChild is not None and root.rightChild is not None:
        return (isFullTree(root.leftChild) and isFullTree(root.rightChild))

    return False

root = Node(1)
root.rightChild = Node(3)
root.leftChild = Node(2)

root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.leftChild.rightChild.leftChild = Node(6)
root.leftChild.rightChild.rightChild = Node(7)

if isFullTree(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")
```