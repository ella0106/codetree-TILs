dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
n, m = map(int, input().split(' '))

array = [
    [0] * m
    for _ in range(n)
]

x, y, d = 0, 0, 0
array[x][y] = 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

for i in range(2, n*m + 1):
    nx, ny = x + dx[d], y + dy[d]
    if not in_range(nx, ny) or array[nx][ny] != 0:
        d = (d + 1) % 4
        
    x, y = x + dx[d], y + dy[d]
    array[x][y] = i

for i in range(n):
    for j in range(m):
        print(array[i][j], end = ' ')
    print()