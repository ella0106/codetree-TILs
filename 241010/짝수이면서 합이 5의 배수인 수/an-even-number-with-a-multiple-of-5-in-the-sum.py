def is_num(n):
    n_sum = int(n[0]) + int(n[1])
    n = int(n)
    return n % 2 == 0 and n_sum % 5 == 0

if is_num(input()):
    print('Yes')
else:
    print('No')