def is_yoon(n):
    if n % 100 == 0 and n % 400 != 0:
        return False
    if n % 4 == 0:
        return True
    return False

print(is_yoon(int(input())))