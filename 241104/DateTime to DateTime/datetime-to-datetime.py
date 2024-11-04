a, b, c = tuple(map(int, input().split()))
day, hour, minute = 11, 11, 11
elapsed = 0
if day > a or hour > b or minute > c:
    print(-1)
else:
    while True:
        if day == a and hour == b and minute == c:
            break

        minute += 1
        elapsed += 1

        if minute == 60:
            minute = 0
            hour += 1
        
        if hour == 24:
            hour = 0
            day += 1

    print(elapsed)