"""
concatenation of two linked list A and B
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

    def concatenate(self, target_list):
        current = self.head
        target_head = target_list.head

        while current.next:
            current = current.next

        current.next = target_head

    def print(self):
        """Prints the linked list"""
        ptr = self.head
        while ptr:
            print(ptr.data, " --> ", end=" ")
            ptr = ptr.next
        print("\n")


if __name__ == "__main__":
    A = [20, 18, 4, 12, 8, 8, 12, 55, 55, 55, 99, 124]

    B = [987, 180, 54, 112, 28, 83, 112, 455, 55, 155, 299]

    print("A :", A)

    list_A = LinkedList()

    list_B = LinkedList()

    for num in A:
        list_A.append(num)

    for num in B:
        list_B.append(num)

    list_A.print()

    list_B.print()

    list_A.concatenate(list_B)

    list_A.print()

    list_B.print()
