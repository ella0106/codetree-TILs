a=input().split(' ')
n, t = int(a[0]), int(a[1])
a = input().split(' ')
x, y, d = int(a[1]), int(a[0]), a[2]
# print(n, t, x, y, d)

dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
mapper = {
    'R':0,
    'U':1,
    'D':2,
    'L':3
}
d = mapper[d]
def in_range(x, y):
    return 1 <= x and x < n+1 and 1 <= y and y < n+1

for i in range(t):
    nx, ny = x + dx[d], y + dy[d]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        d = 3 - d
        # x, y = x + dx[d], y + dy[d]
    # print(x, y)

print(y, x)