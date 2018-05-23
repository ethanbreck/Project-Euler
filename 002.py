def fib(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b


if fib(4000000) % 2 == 0:
