a, b = tuple(map(int, input().split()))
def has_num(n):
    n = str(n)
    n_list = [n[0], n[1]]
    num_list = ['3', '6', '9']
    for num in num_list:
        if num in n_list:
            return True
    return False


def is_magic_number(n):
    return n % 3 == 0 or has_num(n)

cnt = 0
for i in range(a, b+1):
    if is_magic_number(i):
        cnt += 1
print(cnt)