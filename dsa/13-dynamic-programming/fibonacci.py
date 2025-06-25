# this grows exponentially
def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)


# this is much much faster; caching the calculation helps in reusing it for future calculations
def FasterFibonacci(n):
    F = [0, 1] + [None for i in range(n-1)]
    print(F)

    for i in range(2, len(F)):
        F[i] = F[i-1] + F[i-2]

    return F[n]


# 0 1 1 2 3 5 8
print(Fibonacci(6))

print(FasterFibonacci(6))
