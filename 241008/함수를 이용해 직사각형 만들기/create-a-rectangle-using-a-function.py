def p(n, m):
    for _ in range(n):
        print('1'*m)

(n, m) = input().split()
p(int(n), int(m))