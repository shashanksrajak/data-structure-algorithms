"""
Simple bitwise operations - we can manipulate the bits of a variable and 
this is helpful in certain problem solving methods. Few examples are given below and 
more problems are there in this directory.
"""


if __name__ == "__main__":
    A = 12
    B = 1

    print("Value of a: ", A)
    print("Value of a (binary): ", bin(A))
    print("Value of b (binary): ", bin(B))

    # # Bit Masking
    # Let's say that we want to check if Nth bit of A is on or off

    B = B << 2
    print("Value of B after left shifting", B, bin(B))

    # and operation for bitwise
    C = A & B
    print("A&B", C, bin(C))

    # since C is non zero, in fact it is B => the 3rd bit in A is ON

    # check 2nd bit which is 0
    B = 1
    B = B << 1
    print(A & B)  # this prints 0 which means the 2nd bit is OFF
