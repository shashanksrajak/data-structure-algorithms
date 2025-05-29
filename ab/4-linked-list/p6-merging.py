"""
Given two sorted singly linked lists A and B, merge the two lists without using another list
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

    def merge(self, B):
        ptr_a = self.head
        ptr_b = B.head

        while ptr_a or ptr_b:
            if ptr_a.data < ptr_b.data:
                prev = ptr_a
                while ptr_a or ptr_a.data > ptr_b.data:
                    pass

    def print(self):
        """Prints the linked list"""
        ptr = self.head
        while ptr:
            print(ptr.data, " --> ", end=" ")
            ptr = ptr.next
        print("\n")


if __name__ == "__main__":
    A = [20, 18, 4, 12, 8, 8, 12, 55, 55, 55, 99, 124].sort()

    B = [987, 180, 54, 112, 28, 83, 112, 455, 55, 155, 299].sort()

    print("A :", A)
    print("B :", B)

    list_A = LinkedList()

    list_B = LinkedList()

    for num in A:
        list_A.append(num)

    for num in B:
        list_B.append(num)

    list_A.print()

    list_B.print()

    list_A.merge(list_B)

    list_A.print()
