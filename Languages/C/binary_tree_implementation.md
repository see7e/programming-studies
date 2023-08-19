---
title: C - Binary Tree - Implementation
tags: studies, programação
use: Documentation
languages: C
dependences: NULL
---

<details> <summary>Table of Contents</summary>

- [Code File #](#code-file-)
- [Explanation](#explanation)
  - [Section 1: Struct Node Definition](#section-1-struct-node-definition)
  - [Section 2: Create New Node Function](#section-2-create-new-node-function)
  - [Section 3: Check Full Binary Tree Function](#section-3-check-full-binary-tree-function)
  - [Section 4: Main](#section-4-main)
- [Found in Programiz](#found-in-programiz)

</details>

---

# Code File [#](binary_tree.c)
> ChatGPT

The [code](#found-in-programiz) provided appears to have a logical error rather than bugs. The issue lies in the way you're creating nodes and checking for full binary tree property.

In the `createNewNode` function, the `item` field is declared as an `int`, but you're passing a `char` argument (`k`). It's recommended to change the type of `item` to `int` to match the argument type.

To check if a binary tree is a full binary tree, you need to ensure that every node has either zero children or two children. However, in your code, you're using the `item` field to store the node values instead of counting the number of children.

To fix the code, you can modify the structure definition and the `createNewNode` function as follows:

```c
struct Node {
int data;
struct Node *left, *right;
};
```

```c
struct Node *createNewNode(int k) {
struct Node *node = (struct Node *)malloc(sizeof(struct Node));
node->data = k;
node->right = node->left = NULL;
return node;
}
```

Additionally, you can update the `isFullBinaryTree` function to correctly check for the full binary tree property:

```c
bool isFullBinaryTree(struct Node *root) {
if (root == NULL)
return true;

if (root->left == NULL && root->right == NULL)
return true;

if (root->left && root->right)
return (isFullBinaryTree(root->left) && isFullBinaryTree(root->right));

return false;
}
```

With these changes, the code should now work correctly and determine if the given binary tree is a full binary tree.

# Explanation
> ChatGPT powered

This [code](binary_tree.c) defines the struct Node with an int field called data, which stores the value of each node. The createNewNode function creates a new node with the provided value.

The isFullBinaryTree function checks if a given binary tree is a full binary tree by recursively examining each node's children. The main function creates a binary tree with nodes and calls the isFullBinaryTree function to determine if it's a full binary tree or not.

Please note that this code assumes that the tree is a binary tree (each node can have at most two children) and not a binary search tree (BST).

## Section 1: Struct Node Definition

```c
struct Node {
    int data;               // Value stored in the node
    struct Node* left;      // Pointer to the left child
    struct Node* right;     // Pointer to the right child
};
```

In this section, we define a structure called "Node." A structure is like a blueprint that describes what a node of a binary tree should look like. Each node has three parts: `data`, which holds a value, and `left` and `right`, which are like arrows pointing to other nodes. These arrows help us connect the nodes together to form a tree-like structure.

## Section 2: Create New Node Function

```c
struct Node* createNewNode(int k) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = k;
    node->left = node->right = NULL;    // Initialize left and right child pointers as NULL
    return node;
}
```

This section shows a function called `createNewNode` that creates a new node for the binary tree. The function takes a number `k` as input, which represents the value we want to store in the new node. It then creates space in the computer's memory for the new node using `malloc`. After that, it assigns the value `k` to the `data` part of the node, and sets the `left` and `right` pointers to `NULL`, which means there are no other nodes connected to this node yet. Finally, the function returns the newly created node.

## Section 3: Check Full Binary Tree Function

```c
bool isFullBinaryTree(struct Node* root) {
    if (root == NULL)
        return true;    // An empty tree is considered a full binary tree

    if (root->left == NULL && root->right == NULL)
        return true;    // A node without any children is a full binary tree

    if (root->left && root->right)
        return (isFullBinaryTree(root->left) && isFullBinaryTree(root->right));
        // Recursively check if both the left and right subtrees are full binary trees

    return false;       // If none of the above conditions are met, it's not a full binary tree
}
```

This section defines a function called `isFullBinaryTree` that checks if a given binary tree is a full binary tree. It takes a node `root` as input, which represents the starting point of the tree.

First, it checks if the `root` is `NULL`, which means the tree is empty. In that case, it returns `true` because an empty tree is considered a full binary tree.

Next, it checks if the `root` has no left and right children. If that's the case, it means the `root` is a leaf node without any children, and a tree with only one node is also considered a full binary tree. So, it returns `true` in this case.

Then, it checks if both the left and right pointers of the `root` are not `NULL`. This means that the `root` has both left and right children. In that case, it calls the `isFullBinaryTree` function recursively on both the left and right children of the `root`. This recursive call checks if the left and right subtrees are also full binary trees. If both subtrees are full binary trees, it returns `true`.

Finally, if none of the above conditions are met, it means the tree is not a full binary tree, so it returns `false`.

## Section 4: Main

Function

```c
int main() {
    struct Node* root = NULL;

    // Create the binary tree
    root = createNewNode(1);
    root->left = createNewNode(2);
    root->right = createNewNode(3);
    root->left->left = createNewNode(4);
    root->left->right = createNewNode(5);
    root->left->right->left = createNewNode(6);
    root->left->right->right = createNewNode(7);

    // Check if the tree is a full binary tree and print the result
    if (isFullBinaryTree(root))
        printf("The tree is a full binary tree\n");
    else
        printf("The tree is not a full binary tree\n");

    return 0;
}
```

This is the main part of the code. It's like the boss that controls everything!

First, we create a pointer called `root` and set it to `NULL`, which means there is no tree at the beginning.

Then, we start creating nodes and connecting them together to form a binary tree. For example, we create a node with a value of 1 and assign it to the `root`. Then, we create more nodes and connect them to the `root` using the `left` and `right` pointers. It's like building the branches of a tree by connecting the nodes.

After creating the tree, we call the `isFullBinaryTree` function and pass the `root` node as an argument to check if the tree is a full binary tree or not. Depending on the result, we print a message saying whether the tree is a full binary tree or not.

Finally, we return `0` to tell the computer that everything went well and we're done.

That's it! We have explained each section of the code in a simpler way.

# Found in [Programiz](https://www.programiz.com/dsa/full-binary-tree#c-code)

```c
// Checking if a binary tree is a full binary tree in C

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

struct Node {
	int item;
	struct Node *left, *right;
};

// Creation of new Node
struct Node *createNewNode(char k) {
	struct Node *node = (struct Node *)malloc(sizeof(struct Node));
	node->item = k;
	node->right = node->left = NULL;
	return node;
}

bool isFullBinaryTree(struct Node *root) {
	// Checking tree emptiness
	if (root == NULL)
		return true;

	// Checking the presence of children
	if (root->left == NULL && root->right == NULL)
		return true;

	if ((root->left) && (root->right))
		return (isFullBinaryTree(root->left) && isFullBinaryTree(root->right));

	return false;
}

int main() {
	struct Node *root = NULL;
	root = createNewNode(1);
	root->left = createNewNode(2);
	root->right = createNewNode(3);

	root->left->left = createNewNode(4);
	root->left->right = createNewNode(5);
	root->left->right->left = createNewNode(6);
	root->left->right->right = createNewNode(7);

	if (isFullBinaryTree(root))
		printf("The tree is a full binary tree\n");
	else
		printf("The tree is not a full binary tree\n");
}
```