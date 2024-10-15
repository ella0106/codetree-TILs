a, b = tuple(map(int, input().split()))
def answer(a, b):
    if a > b:
        a += 25
        b *= 2
    else:
        a *= 2
        b += 25
    print('{} {}'.format(a, b))

answer(a, b)