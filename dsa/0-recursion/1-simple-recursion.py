def func2(n):
    if n > 0:
        # recurive call to same function
        func2(n-1)
        # this will be executed when last function starts returning
        print(n)


if __name__ == "__main__":
    func2(5)
