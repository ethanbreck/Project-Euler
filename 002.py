
def fib():
    x = 0
    y = 1
    while True:
        yield x
        x, y = y, x + y


for fib in range(4000000):
    sum(fib)
    print(sum)
