"""
Given a singly linked list, check if it is sorted or not.
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

    def is_sorted(self):
        if self.length == 1:
            return True

        x = self.head.data
        current = self.head

        while current:
            if current.data >= x:
                x = current.data
                current = current.next
            else:
                return False
        return True

    def print(self):
        """Prints the linked list"""
        ptr = self.head
        while ptr:
            print(ptr.data, " --> ", end=" ")
            ptr = ptr.next
        print("\n")


if __name__ == "__main__":
    A = [20, 18, 4, 12, 55, 99, 124]
    B = [20, 18, 4, 12, 55, 99, 124]

    A.sort()

    print("A :", A)
    print("B: ", B)

    linked_list = LinkedList()

    for num in B:
        linked_list.append(num)

    linked_list.print()

    print("Is list sorted", linked_list.is_sorted())
