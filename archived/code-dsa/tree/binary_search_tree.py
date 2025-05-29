# as compared to Binary Tree, Binary Search Tree works recursively

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

    def find_max(self):
        if self.right is None:
            return self.data

        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data

        return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
            # else:
            #     # element does not exist
            #       python by default returns None
            #     return None
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)

        return self


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
    bst.delete(23)
    print(bst.in_order_traversal())
