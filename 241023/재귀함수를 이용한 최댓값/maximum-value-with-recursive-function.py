n = int(input())
arr = list(map(int, input().split()))
def p(n, arr):
    if n == 0:
        return arr[n]
    else:
        return max(p(n-1, arr), arr[n])

print(p(n-1, arr))