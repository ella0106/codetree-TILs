m1, d1, m2, d2 = tuple(map(int, input().split()))
months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d1 += 5
days = 0
for m in range(m1, m2):
    days += months[m]
    #print(m, days)

days += d2
days -= d1
#print(days)

print(days // 7 + 1)