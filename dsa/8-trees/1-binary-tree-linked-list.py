"""
Create a Binary Tree using Linked List representation
"""

# We will need - Linked List, Queue

# Note that this implementation is bit different from a Linear Data Structure (e.g. doubly linked list)

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self, data):
        # create a new node
        node = Node(data)
        self.root = node
        self.queue = deque()
        self.queue.append(self.root)

    def insert_left(self, data, parent: Node):
        # create a new node
        node = Node(data)
        parent.left_child = node
        self.queue.append(node)

    def insert_right(self, data, parent: Node):
        # create a new node
        node = Node(data)
        parent.right_child = node
        self.queue.append(node)

    def traversal_preorder(self, node: Node):
        if node is not None:
            print(node.data, end=" -- ")

            self.traversal_preorder(node.left_child)
            self.traversal_preorder(node.right_child)

    def traversal_inorder(self, node: Node):
        if node is not None:
            self.traversal_inorder(node.left_child)
            print(node.data, end=" -- ")
            self.traversal_inorder(node.right_child)


if __name__ == "__main__":
    tree = BinaryTree(10)

    print(tree.root.data)

    print("Lets create a Binary Tree: ")

    while tree.queue:
        current_node = tree.queue.popleft()
        try:
            x = int(input(
                f"Enter left child for node with data {current_node.data}  (enter if its NULL) : "))
            tree.insert_left(x, current_node)
        except:
            pass

        try:
            x = int(input(
                f"Enter right child for node with data {current_node.data}  (enter if its NULL) : "))
            tree.insert_right(x, current_node)
        except:
            pass

    print("Root node data", tree.root.data)

    print("Pre-order traversal----")
    tree.traversal_preorder(tree.root)
