def p1(n):
    if n == 0:
        return
    else:
        p1(n-1)
        print(n, end=" ")


def p2(n):
    if n == 0:
        return
    else:
        print(n, end=" ")
        p2(n-1)

n = int(input())
p1(n)
print()
p2(n)