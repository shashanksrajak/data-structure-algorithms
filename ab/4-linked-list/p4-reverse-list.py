"""
Given a singly linked list, reverse the list. 

Reverse can happen in 2 ways - either reverse the elements or reverse the links. 
We will do the later one.
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

    def reverse(self):

        prev = None
        current = self.head
        leader = self.head.next

        while current.next:
            current.next = prev  # reversed
            prev = current
            current = leader
            leader = leader.next

        current.next = prev
        self.head = current

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

    linked_list.reverse()

    linked_list.print()
