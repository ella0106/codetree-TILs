def p(n):
    if n==1:
        return 1
    else:
        return p(n-1)+n

print(p(int(input())))