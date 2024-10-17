a,b=tuple(map(int, input().split()))
def answer(a,b):
    if b > a:
        a += 10
        b *= 2
    else:
        b += 10
        a *= 2
    print(a, b)

answer(a,b)