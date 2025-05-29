"""
Check if parenthesis in an expression are balanced.
"""


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
        x = -1
        if self.height > 0:
            self.height -= 1
            self.top -= 1
            x = self.items.pop()
        return x

    def peek(self, pos):
        pass

    def is_empty(self):
        return True if self.top == -1 else False

    def __repr__(self):
        return f"Stack(\n  top:{self.top},\n  height:{self.height}\n  items: {self.items}\n)"


"""
T: O(n) for travelling through all the chars 
"""


def check_balanced(expression: str):
    stack = Stack()

    for char in expression:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.is_empty():
                # there is no opening ( for a closing ) => imbalanced
                return False
            else:
                stack.pop()

    # if going through all the () stack is still occupied then also its imbalanced
    if stack.is_empty():
        return True
    else:
        return False


if __name__ == "__main__":
    expression = "(a+b)*(c+d)"
    # expression = "(a+b)*()c+d)"
    # expression = "(a+b)*()(c+d)"

    print(f"Is this expr {expression} balanced?", check_balanced(expression))
