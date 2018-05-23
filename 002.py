def fib(n):
    a, b = 0, 1
    old_a = 0
    while a < n:
        old_a = a
        a, b = b, a + b
        print(old_a)
    return old_a


print(fib(40))
