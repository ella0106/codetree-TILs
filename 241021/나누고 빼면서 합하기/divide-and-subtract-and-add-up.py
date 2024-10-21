n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def answer(m):
    h = 0
    while m > 0:
        h += arr[m-1]
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    print(h)

answer(m)