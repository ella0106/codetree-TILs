m1, d1, m2, d2 = tuple(map(int, input().split()))
months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d1 += 5
cnt = 1
while True:
    if m1 >= m2 and d1 >= d2:
        break

    if d1 > months[m1]:
        d1 -= months[m1]
        m1 += 1

    d1 += 7
    cnt += 1
    # print(m1, d1, m2, d2)

print(cnt)