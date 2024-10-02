num = int(input())
mapper = {
    'N' : [0, 1],
    'S' : [0, -1],
    'E' : [1, 0],
    'W' : [-1, 0]
}

x, y = 0, 0
cnt = 0
answer = 0

for i in range(num):
    a = input().split()
    for j in range(int(a[1])):
        cnt += 1
        x, y = x + mapper[a[0]][0], y + mapper[a[0]][1]
        if x == 0 and y == 0:
            answer = cnt
            break
    if x == 0 and y == 0:
        break

if answer == 0:
    print(-1)
else:
    print(answer)