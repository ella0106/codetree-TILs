def p(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return p(n//3) + p(n-1)

print(p(int(input())))