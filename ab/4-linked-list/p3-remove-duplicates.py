"""
Remove duplicates from a sorted linked list (singly)
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

    def remove_duplicates(self):

        prev = self.head
        current = self.head.next

        while current:
            if current.data != prev.data:
                prev = current
                current = current.next
            else:
                prev.next = current.next
                current = prev.next

    def print(self):
        """Prints the linked list"""
        ptr = self.head
        while ptr:
            print(ptr.data, " --> ", end=" ")
            ptr = ptr.next
        print("\n")


if __name__ == "__main__":
    A = [20, 18, 4, 12, 8, 8, 12, 55, 55, 55, 99, 124]

    A.sort()

    print("A :", A)

    linked_list = LinkedList()

    for num in A:
        linked_list.append(num)

    linked_list.print()

    linked_list.remove_duplicates()

    linked_list.print()
