# Binary search tree exercise
# Link

# Solution

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # handle duplicate values
        if data == self.data:
            return

        if data < self.data:
            # add in the left side
            if self.left:
                # recursion
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add in the right side
            if self.right:
                # recursion
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left node
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # find in left tree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # find in right tree
            if self.right:
                return self.right.search(val)
            else:
                return False


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 5, 18]
    bst = build_tree(numbers)
    print(bst.in_order_traversal())
    print(bst.search(18))
