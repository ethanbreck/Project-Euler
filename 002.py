
def fib(max):
    x = 0
    y = 1
    while x < 4000000:
        yield x
        x, y = y, x + y
