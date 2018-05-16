def fib(i):
    old_a = 0
    a = 0
    b = 1
    while a < i:
        yield a
        old_a = a
        a = b
        b = old_a+b
        print(a)


print(fib(100))
