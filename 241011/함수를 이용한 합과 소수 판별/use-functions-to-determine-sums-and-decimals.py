def is_sosu(n):
    for i in range(2, n+1):
        if n % i == 0:
            return False
    return True

def is_even(n):
    n = str(n)
    total = 0
    for i in range(len(n)):
        total += n[i]
    if total % 2 == 0:
        return True
    return False

a, b = tuple(map(int, input().split()))
cnt = 0
for i in range(a, b+1):
    if is_sosu(i) and is_even(i):
        cnt += 1

print(cnt)