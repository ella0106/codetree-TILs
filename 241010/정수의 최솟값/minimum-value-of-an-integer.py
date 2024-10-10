def m(a, b, c,):
    return min(a, b, c)

a, b, c = tuple(map(int, input().split()))
print(m(a, b, c))