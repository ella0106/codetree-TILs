(n, m) = input().split(' ')
def gong(n, m):
    result = 0
    for i in range(1, min(n, m)+1):
        if n % i == 0 and m % i == 0:
            result = max(result, i)

    print(result)

gong(int(n), int(m))