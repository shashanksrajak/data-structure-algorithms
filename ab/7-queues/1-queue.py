"Queue implementation using a Linked List"


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Add a new node in queue in the last, FIFO
        """
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        """
        Remove the first element in the Queue from beginning
        """
        x = None
        if self.is_empty():
            x = None
        elif self.size == 1:
            x = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            x = self.head.data
            self.head = self.head.next
            self.size -= 1
        return x

    def is_empty(self):
        return True if self.size == 0 else False

    def print(self):
        ptr = self.head
        print("Head <--", end="")
        while ptr:
            print(f"<-- {ptr.data}", end="")
            ptr = ptr.next
        print("<--Tail")


if __name__ == "__main__":
    A = [12, 14, 21, 34, 56, 78, 92, 22]

    queue = Queue()
    for a in A:
        queue.enqueue(a)

    queue.print()

    print("Dequeue element - ", queue.dequeue())

    print("Size of the queue is - ", queue.size)
