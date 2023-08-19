class Node:
	def __init__(self, item):
		self.item = item
		self.leftChild = None
		self.rightChild = None

def isFullTree(root):
	if root is None:  # Tree empty case
		return True

	if root.leftChild is None and root.rightChild is None:  # Checking whether child is present
		return True

	if root.leftChild is None or root.rightChild is None:  # If either child is absent (not both), return False
		return False

	return isFullTree(root.leftChild) and isFullTree(root.rightChild)  # Recursively check left and right subtrees

root = Node(1)
root.leftChild = Node(2)
root.rightChild = Node(3)
root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.rightChild.leftChild = Node(6)
root.rightChild.rightChild = Node(7)

if isFullTree(root):
	print("The tree is a full binary tree")
else:
	print("The tree is not a full binary tree")
