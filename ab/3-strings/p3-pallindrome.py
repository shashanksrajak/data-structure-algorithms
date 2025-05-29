"""
Find pallindrome of a string. Also some string comparision.
"""


def pallindrome(s):
    if not s:
        return

    i, j = 0, len(s)-1

    while i < j:
        if s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1

    return True


def compare(s1, s2):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        elif s1[i] > s2[j]:
            return f"{s1} > {s2}"
        else:
            return f"{s2} > {s1}"

    if len(s1) == len(s2):
        return "equal"
    elif len(s1) > len(s2):
        return f"{s1} > {s2}"
    else:
        return f"{s2} > {s1}"


def compare_pythonic(s1, s2):
    if s1 == s2:
        return "Equal"
    elif s1 > s2:
        return f"{s1} > {s2}"
    else:
        return f"{s2} > {s1}"


if __name__ == "__main__":
    s1 = "Shashank Rajak"
    s2 = "Madam"
    s3 = "Madamw"

    print("Original String: ", s1)

    print("Is Pallindrome?", pallindrome(s1))
    print("Is Pallindrome?", pallindrome(s2))

    print(compare(s3, s2))

    print(compare_pythonic(s3, s2))
