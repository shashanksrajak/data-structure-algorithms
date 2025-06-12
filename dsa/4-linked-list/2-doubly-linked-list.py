class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            # there is no node yet
            self.head = new_node
        else:
            # there are few nodes existing already

            # go to last node
            ptr = self.head
            while ptr.next:
                ptr = ptr.next

            ptr.next = new_node
            new_node.prev = ptr
        self.length += 1

    def print(self):
        ptr = self.head
        while ptr:
            print(ptr.data, "--> ", end="")
            ptr = ptr.next
        print("\n")

    def insert(self, data, index):
        if index < 0 or index > self.length - 1:
            return "Index out of range"

        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            ptr = self.head
            for _ in range(index-1):
                ptr = ptr.next

            new_node.prev = ptr
            new_node.next = ptr.next

            ptr.next.prev = new_node
            ptr.next = new_node

        self.length += 1
        return

    def delete(self, index):
        x = -1
        if index < 0 or index >= self.length:
            return -1

        if index == 0:
            x = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            ptr = self.head
            for _ in range(index-1):
                ptr = ptr.next
            x = ptr.next.data
            ptr.next = ptr.next.next
            if ptr.next:
                ptr.next.next.prev = ptr
        self.length -= 1
        return x


if __name__ == "__main__":
    A = [20, 18, 4, 12, 55, 99, 124]

    print(A)

    dll = DoublyLinkedList()

    for num in A:
        dll.append(num)

    dll.print()

    dll.insert(1888, 1)

    dll.print()

    # print(linked_list)

    print("Delete node at index", dll.delete(1))

    dll.print()
