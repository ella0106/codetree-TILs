n = int(input())
arr = list(map(int, input().split()))
answer = []
for i in range(1, n+1):
    if i % 2 != 0:
        a = arr[:i]
        a.sort()
        print(a[i//2], end=' ')