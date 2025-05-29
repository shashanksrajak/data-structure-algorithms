# In Python, there is no in-build linked list data type, so we need to implement it on our own
# and we are free to design it but usually we use List to implement a Linked List
# also check C code to understand low level operations

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

    def prepend(self, data):
        """Adds a node to the beginning - this will be O(1)"""
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return

    def insert(self, data, index):
        """Inserts a new node at an index, consider 0 based index in linked list"""
        node = Node(data)

        if index < 0 or index > self.length-1:
            return "Index out of range"

        if index == 0:
            self.prepend(data)
        elif index == self.length - 1:
            self.append(data)
        else:
            # inserting somewhere in the middle
            p = self.head
            current_index = 0
            while p:
                if current_index + 1 == index:
                    node.next = p.next
                    p.next = node
                    break
                p = p.next
                current_index += 1

        self.length += 1
        return

    def print(self):
        """Prints the linked list"""
        ptr = self.head
        while ptr:
            print(ptr.data, " --> ", end=" ")
            ptr = ptr.next

    def __repr__(self):
        return f"{self.print()}"

    def delete(self, index):
        x = -1
        if index < 0 or index > self.length-1:
            return x

        if index == 0:
            # delete first node
            x = self.head.data
            self.head = self.head.next

        else:
            ptr = self.head
            counter = 0
            while ptr.next:
                if counter + 1 == index:
                    x = ptr.next.data
                    ptr.next = ptr.next.next
                    break
                ptr = ptr.next
                counter += 1
        self.length -= 1
        return x


if __name__ == "__main__":
    A = [20, 18, 4, 12, 55, 99, 124]

    print(A)

    linked_list = LinkedList()

    for num in A:
        linked_list.append(num)

    # linked_list.print()
    print(linked_list)

    linked_list.insert(1888, 4)

    print(linked_list)

    print("Delete node at index", linked_list.delete(8))

    print(linked_list)
