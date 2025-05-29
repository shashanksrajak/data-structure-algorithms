"""
Reverse a given string
"""


def reverse(s):
    if not s:
        return

    # i, j = 0, len(s)-1

    # while i < j:
    #     s[i], s[j] = s[i], s[j]

    # The above method is not allowed in Python! strings are immutable

    A = [char for char in s]
    i, j = 0, len(A)-1

    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1

    return "".join(A)


if __name__ == "__main__":
    s1 = "Shashank Rajak"

    print("Original String: ", s1)
    r1 = reverse(s1)
    print("Reversed String: ", r1)
