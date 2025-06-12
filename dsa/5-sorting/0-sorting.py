
import functools

A = [10, 1, 3, 6, 8, 24, 54, 67]

print(A)


def comparision_function(x, y):
    if x > y:
        return 1  # sort them
    elif x < y:
        return -1
    else:
        return 0


A.sort(key=lambda x: x > 5)

A.sort(key=functools.cmp_to_key(comparision_function))

print(A)
