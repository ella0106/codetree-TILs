a, b, c = tuple(map(int, input().split()))
n = a*b*c

def p(n):
    if n < 10:
        return n
    else:
        return p(n // 10) + n % 10

print(p(n))