n, m = tuple(map(int, input().split()))
ar = list(map(int, input().split()))

def f(a, b):
    global ar
    total = 0
    for i in range(a-1, b):
        total += ar[i]
    print(total)


for i in range(m):
    a, b = tuple(map(int, input().split()))
    f(a, b)