n = int(input())
arr = list(map(int, input().split()))

def answer(n, arr):
    for i in range(n):
        arr[i] = abs(arr[i])
        print(arr[i], end=' ')

answer(n, arr)