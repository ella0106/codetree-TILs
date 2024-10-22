n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    gcd = 1
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return a * b // gcd

def p(n):
    if n == 0:
        return arr[n]
    else:
        return gcd(p(n-1), arr[n])

print(p(n-1))