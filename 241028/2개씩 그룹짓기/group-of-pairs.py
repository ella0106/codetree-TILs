n = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
for i in range(n):
    tmp = arr[i] + arr[n*2-1-i]
   # print(tmp)
    if tmp > cnt:
        cnt = tmp
    
print(cnt)