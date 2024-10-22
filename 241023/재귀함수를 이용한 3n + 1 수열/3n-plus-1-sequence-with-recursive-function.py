def p(n, cnt=0):
    if n == 1:
        return cnt
    else:
        cnt += 1
        if n % 2 == 0:
            return p(n // 2, cnt)
        else:
            return p(n * 3 + 1, cnt)

print(p(int(input())))