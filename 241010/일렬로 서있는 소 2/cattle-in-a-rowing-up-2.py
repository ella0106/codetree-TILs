n = int(input())
cow = input().split(' ')


ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if int(cow[i]) <= int(cow[j]) and int(cow[j]) <= int(cow[k]):
                ans += 1

print(ans)