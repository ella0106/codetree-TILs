def p(n):
    if n <= 2:
        return 1
    else:
        return p(n-1) + p(n-2)

print(p(int(input())))