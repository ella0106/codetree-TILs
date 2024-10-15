a, b = tuple(map(int, input().split()))
def answer(a, b):
    m = max(a, b)
    m += 25
    mi = min(a, b)
    mi *= 2
    print('{} {}'.format(mi, m))

answer(a, b)