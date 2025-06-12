# Source: EPI 8.2
# Difficulty: Easy
# Topic: Stacks
# Tags: tag1, tag2
# Related Concepts: ..
# Question: ..
"""
Write a program to evaluate a postfix mathematical expression "32, 3, +, 2, *, 1, +"
"""

"""
T: O(n)
"""


def evaluate_postfix(expr: str):

    elements = expr.split(",")  # comma is delimiter
    stack = []

    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "/": lambda x, y: x/y,
        "*": lambda x, y: x*y
    }

    for element in elements:
        if element in operators:
            y = stack.pop()
            x = stack.pop()
            result = operators[element](x, y)
            stack.append(result)
        else:
            # lets assume that we dont have any element other than numbers
            # if its a number we push into the stack
            stack.append(int(element))

    return stack.pop()


if __name__ == "__main__":
    expr = "1,1,+,-2,*"
    # expr = "3,4,+,2,*,1,+"

    result = evaluate_postfix(expr)
    print(f"The result of {expr} is: ", result)
