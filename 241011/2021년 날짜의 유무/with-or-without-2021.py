days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m, d = tuple(map(int, input().split()))

def is_there(m, d):
    if m > 12 or d > days[m]:
        return 'No'
    return 'Yes'

print(is_there(m,d))