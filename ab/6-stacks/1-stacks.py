
class Stack:
    def __init__(self):
        self.top = -1
        self.height = 0
        self.items = []

    def print(self):
        for i in range(self.height):
            print(self.items[i])

    def push(self, data):
        self.items.append(data)
        self.height += 1
        self.top += 1

    def pop(self):
        x = None
        if self.height > 0:
            self.height -= 1
            self.top -= 1
            x = self.items.pop()
        return x

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1]

    def is_empty(self):
        return False if self.height != 0 else True

    def __repr__(self):
        return f"Stack(\n  top:{self.top},\n  height:{self.height}\n  items: {self.items}\n)"


if __name__ == "__main__":
    stack = Stack()

    nums = [14, 12, 3, 90, 8, 66, 24]

    print(nums)

    for num in nums:
        stack.push(num)

    print(stack)

    print(stack.pop())
    print(stack)
