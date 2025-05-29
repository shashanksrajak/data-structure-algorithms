# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/3_LinkedList/3_linked_list_exercise.md#exercise-linked-list


# Implement a Doubly Linked List

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        node = Node(data)

        # in case it is very first node inserted, then that becomes tail as well
        if (self.head == None):
            self.tail = node
            self.head = node
            return

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        return

    def print_forward(self):
        itr = self.head
        print("Forward Printing List")

        while (itr):
            print(itr.data, end="->")
            itr = itr.next
        print("\n")
        return

    def print_backward(self):
        itr = self.tail
        print("Backward Printing List")

        while (itr):
            print(itr.data, end="->")
            itr = itr.prev
        print("\n")
        return


# Initialise a doubly linked list
dll = DoublyLinkedList()

# insert data
dll.insert_at_start(7)
dll.insert_at_start(21)
dll.insert_at_start(123)


dll.print_forward()

dll.print_backward()
