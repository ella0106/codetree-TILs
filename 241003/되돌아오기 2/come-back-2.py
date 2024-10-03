road = input()
mapper = {
    'F' : 0,
    'R' : 1,
    'L' : -1,
}

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y, dir_num = 0, 0, 0

for i in range(len(road)):
    change = mapper[road[i]]
    if change == 0:
        x, y = x + dx[dir_num], y + dy[dir_num]
    else:
        dir_num += mapper[road[i]]
        dir_num = (4 + dir_num) % 4
    if x == 0 and y == 0:
        print(i+1)
        break

if x != 0 or y != 0:
    print(-1)