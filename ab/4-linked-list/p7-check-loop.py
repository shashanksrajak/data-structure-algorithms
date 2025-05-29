"""
Find loop in a linked list. FAQ in linked list.

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

    def check_loop(self, B):
        # take two pointers
        fast = self.head  # move 2 steps
        slow = self.head  # move 1 step

        while slow and fast and fast != slow:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next

        return True if fast == slow else False

    def introduce_loop(self, target_index):
        pass

    def print(self):
        """Prints the linked list"""
        ptr = self.head
        while ptr:
            print(ptr.data, " --> ", end=" ")
            ptr = ptr.next
        print("\n")


if __name__ == "__main__":
    A = [20, 18, 4, 12, 8, 8, 12, 55, 55, 55, 99, 124]
    print("A :", A)

    list_A = LinkedList()

    for num in A:
        list_A.append(num)

    list_A.print()

    list_A.introduce_loop()

    list_A.print()
