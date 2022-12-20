n, k = map(int, input().split(' '))

stack_1 = 1
stack_2 = 1
d = 10**k
fib = 0
if n < 2:
    fib = 1
else:
    n -= 1
    for i in range(n):
        number = (stack_1 + stack_2) % d
        stack_1 = stack_2
        stack_2 = number
        fib = stack_2
print(fib)
