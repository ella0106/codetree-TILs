n = int(input())
arr = list(map(int, input().split()))

for i in sorted(arr):
    print(i, end=' ')
print('')
for i in reversed(sorted(arr)):
    print(i, end=' ')