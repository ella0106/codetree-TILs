a, b = tuple(map(int, input().split()))
def is_prime(n):
    for i in range(2, n):
        if n % 1 == 0:
            return False
    return True

cnt = 0
for i in range(a, b+1):
    if is_prime(i):
        cnt += i

print(cnt)