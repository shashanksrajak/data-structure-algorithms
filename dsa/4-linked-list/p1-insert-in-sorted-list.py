"""
Given a sorted (asc) linked list e.g. 3->7->9->15->20->None
Insert a new node 18 at its sorted position i.e. ->15->18->20->None

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        """Adding a new node at the last- this will be O(n) because we need to go to last node"""
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            # go to last node and add
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = node
        self.length += 1
        return

    def insert_sorted(self, data):
        """Inserts a new node at an index, consider 0 based index in linked list"""
        new_node = Node(data)

        prev, current = None, self.head

        while current and current.data < data:
            prev = current
            current = current.next

        # insert after prev node
        # check if its first node
        if prev is None:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = current
            prev.next = new_node
        self.length += 1
        return

    def print(self):
        """Prints the linked list"""
        print("\n")
        ptr = self.head
        while ptr:
            print(ptr.data, " --> ", end=" ")
            ptr = ptr.next


if __name__ == "__main__":
    A = [20, 18, 4, 12, 55, 99, 124]

    A.sort()

    print(A)

    linked_list = LinkedList()

    for num in A:
        linked_list.append(num)

    linked_list.print()

    linked_list.insert_sorted(12)

    linked_list.print()
