#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;               // Value stored in the node
    struct Node* left;      // Pointer to the left child
    struct Node* right;     // Pointer to the right child
};

// Function to create a new node with the given value
struct Node* createNewNode(int k) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = k;
    node->left = node->right = NULL;    // Initialize left and right child pointers as NULL
    return node;
}

// Function to check if a binary tree is a full binary tree
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
