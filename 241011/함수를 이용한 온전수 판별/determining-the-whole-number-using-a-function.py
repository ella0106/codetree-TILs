def is_onjeon(n):
    if n % 2 == 0:
        return False
    if str(n)[-1] == '5':
        return False
    if n % 3 == 0 and n % 9 != 0:
        return False
    return True

a, b = tuple(map(int, input().split()))
cnt = 0
for i in range(a, b+1):
    if is_onjeon(i):
        # print(i)
        cnt += 1

print(cnt)