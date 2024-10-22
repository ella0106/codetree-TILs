def p(n):
    if n < 10:
        return n**2
    else:
        return p(n//10) + (n%10)**2

print(p(int(input())))