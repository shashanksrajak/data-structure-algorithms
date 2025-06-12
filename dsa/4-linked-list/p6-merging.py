# Source: https://neetcode.io/problems/merge-two-sorted-linked-lists?list=blind75
# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Difficulty: Easy
# Topic: Arrays
# Tags: tag1, tag2
# Related Concepts: ..
# Question: ..


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

    def merge(self, list2: Node):
        """
        this is quite descriptive code, we can also use a simple dummy node and solve using it
        check the NeetCode solution in above link
        """
        list1 = self.head

        if not list1:
            return list2
        if not list2:
            return list1

        last = Node(-1)

        if list1.data <= list2.data:
            self.head = list1
        else:
            self.head = list2

        while list1 and list2:
            if list1.data <= list2.data:
                last.next = list1
                last = list1
                list1 = list1.next
                last.next = None
            else:
                last.next = list2
                last = list2
                list2 = list2.next
                last.next = None

        if list1:
            last.next = list1
        else:
            last.next = list2

        return self.head

    def print(self):
        """Prints the linked list"""
        ptr = self.head
        while ptr:
            print(ptr.data, " --> ", end=" ")
            ptr = ptr.next
        print("\n")


if __name__ == "__main__":
    A = [3, 4, 5]

    B = [4, 5, 6]

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

    list_A.merge(list_B.head)

    list_A.print()

    list_B.print()
