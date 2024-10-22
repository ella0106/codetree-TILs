def p(n):
    if n <= 2:
        return n
    else:
        return p(n-2) + n

print(p(int(input())))