y, m, d = tuple(map(int, input().split()))

def is_yoon(y):
    if y % 400 == 0:
        return True
    if y % 4 == 0 and y % 100 != 0:
        return True
    return False

def is_date(y, m, d):
    day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m == 2 and is_yoon(y):
        if d <= day[m]+1:
            return True
        else:
            return False
    else:
        if d <= day[m]:
            return True
        else:
            return False

if is_date(y, m, d):
    if 3 <= m and m <= 5:
        print('Spring')
    elif 6 <= m and m <= 8:
        print('Summer')
    elif 9 <= m and m <= 11:
        print('Fall')
    else:
        print('Winter')

else:
    print(-1)