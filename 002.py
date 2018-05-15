
def fib(max):
    x = 0
    y = 1
    while max > x:
        yield x
        x, y = y, x + y


for max in range(4000000):
    sum(fib)
    print(sum)
