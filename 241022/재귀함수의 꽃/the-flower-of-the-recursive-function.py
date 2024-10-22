def p(n):
    if n == 0:
        return
    else:
        print(n, end=" ")
        p(n-1)
        print(n, end=" ")

p(int(input()))