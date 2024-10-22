def p(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    else:
        return (p(n-1) * p(n-2)) % 100

print(p(int(input())))