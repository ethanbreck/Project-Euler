def fib(n):
    a, b = 0, 1
    old_a = 0
    while a < n:
        old_a = a
        a, b = b, a + b
        print(old_a)
    return old_a


def fibsum(n):
    a, b = 0, 1
    old_a = 0
    total = 0
    while a < n:
        old_a = a
        a, b = b, a + b
        print(old_a)
        if old_a % 2 == 0:
            total += old_a
        print(total)
    return old_a


fibsum(4000000)
