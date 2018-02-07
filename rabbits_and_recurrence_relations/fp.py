def fib(n, k):
    if n <= 1:
        return 1
    else:
        return fib(n-1, k) + k * fib(n-2, k)

print(fib(28, 3))