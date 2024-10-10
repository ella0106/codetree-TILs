def is_yoon(n):
    if n % 100 == 0 and n % 400 != 0:
        return 'false'
    if n % 4 == 0:
        return 'true'
    return 'false'

print(is_yoon(int(input())))