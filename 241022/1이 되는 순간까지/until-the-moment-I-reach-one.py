def p(n, cnt):
    if n == 1:
        return cnt
    else:
        cnt += 1
        if n % 2 == 0:
            return p(n//2, cnt)
        else:

            return p(n//3, cnt)

print(p(int(input()), 0))