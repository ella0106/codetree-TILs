hour, mins, h2, m2 = tuple(map(int, input().split()))
time = 0

while True:
    if hour == h2 and mins == m2:
        break

    time += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0

print(time)