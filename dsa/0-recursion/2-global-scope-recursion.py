x = 0


def func(n):
    if n > 0:
        global x
        x += 1
        # note that the value of x will be added during returns, not during function calls.
        # since its a global variable so only one x exists and its final value will be used in all
        # the additions
        return func(n-1) + x
    return 0


if __name__ == "__main__":
    print("x before calling func", x)
    n = 5
    output = func(n)
    print("x after calling func", x)
    print("output of func: ", output)
