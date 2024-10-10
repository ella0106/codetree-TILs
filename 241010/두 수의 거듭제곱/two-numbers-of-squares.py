a, b = tuple(map(int, input().split()))
cnt = 1
for i in range(b):
    cnt *= a

print(cnt)