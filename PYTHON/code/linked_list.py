class LinkedListNode:
    def __init__(self, key, val):      # Constructor function that creates a new LinkedListNode
        self.value = val              # Store the value of the node
        self.key = key                # Store the key of the node
        self.next = None              # Initialize the next node to None (there is no next node yet)
    
    def insert(self, key, val):       # Function to insert a new node into the linked list
        node = LinkedListNode(key, val)   # Create a new node
        if self.next == None:         # If there is no next node, add the new node here
            self.next = node
        else:                         # If there is a next node, call the _insert function to find the right place to insert the new node
            self._insert(self.next, node, key, val)

    def _insert(self, curr, node, key, val):   # Recursive helper function to find the right place to insert a new node
        if curr.next == None:         # If we reach the end of the linked list, add the new node here
            curr.next = node
        else:
            self._insert(curr.next, node, key, val)   # Otherwise, keep looking for the right place to insert the new node

    def insertAfterIndex(self, key, val, index: int):   # Function to insert a new node after a specific index in the linked list
        node = LinkedListNode(key, val)   # Create a new node
        i = 0                            # Initialize a counter
        curr = self                      # Start at the beginning of the linked list
        while i != index:                # Keep moving through the linked list until we reach the index we want to insert the new node after
            curr = curr.next
            i += 1
        temp = curr.next                  # Save a reference to the current node's next node
        curr.next = node                  # Insert the new node after the current node
        node.next = temp                   # Set the new node's next node to the current node's old next node
    
    def removeAtIndex(self, index: int):   # Function to remove a node from the linked list at a specific index
        i = 0                             # Initialize a counter
        curr = self                       # Start at the beginning of the linked list
        while i != index-1:               # Keep moving through the linked list until we reach the node just before the one we want to remove
            curr = curr.next
            i += 1
        curr.next = curr.nex.next         # Remove the node by setting the current node's next node to the node after the one we want to remove

    def printList(self):                  # Function to print out all the nodes in the linked list
        lst = []                          # Create an empty list to store the nodes
        lst.append((self.key, self.value))   # Add the current node to the list
        self._printList(self, lst)

    def _printList(self, node, lst):        # Recursive helper function to print out all the nodes in the linked list
        if node.next == None:             # If we've reached the end of the linked list, print out the list and return
            print(lst)
            return
        lst.append((node.next.key, node.next.value))    # Add the next node to the list
        self._printList(node.next, lst)     # Recursively call the _printList function on the next node

# Create a new linked list with a node containing key 'a' and value 1
l = LinkedListNode('a',1)

# Insert a new node with key 'z' and value 2 into the linked list
l.insert('z',2)

# Insert a new node with key 'e' and value 3 into the linked list
l.insert('e',3)

# Insert a new node with key 'w' and value 0 after the first node in the linked list
l.insertAfterIndex('w',0,0)

# Remove the first node from the linked list
l.removeAtIndex(0)

# Print out all the nodes in the linked list
l.printList

        