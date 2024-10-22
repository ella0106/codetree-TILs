def p(n):
    if n == 0:
        return
    else:
        print("* "*n)
        p(n-1)
        print("* "*n)

p(int(input()))