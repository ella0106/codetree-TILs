(n, m)= input().split(' ')
def gong(n, m):
    h = max(n, m)
    r = m*n
    for i in range(h, n*m, 2):
        if i % n == 0 and i % m == 0:
            r = min(r, i)
    print(r)

gong(int(n), int(m))