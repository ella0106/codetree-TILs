n, k, T = tuple(input().split(' '))
Tl = len(T)
arr = []
for i in range(int(n)):
    t = input()
    if T == t[:Tl]:
        arr.append(t)

arr.sort()
print(arr[int(k)-1])