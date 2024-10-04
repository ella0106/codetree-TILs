(n, m) = input().split(' ')
n, m = int(n), int(m)
array = [[0]*n
    for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

for i in range(m):
    (r, c) = input().split(' ')
    r, c = int(r)-1, int(c)-1
    array[r][c] = 1
    cnt = 0
    for j in range(4):
        nx, ny = r + dx[j], c + dy[j]
        if in_range(nx, ny) and array[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)