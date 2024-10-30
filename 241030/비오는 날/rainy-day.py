class Weather:
    def __init__(self, date, week, weather):
        self.date = date
        self.week = week
        self.weather = weather

n = int(input())

ws = []

for _ in range(n):
    date, week, weather = tuple(input().split())
    ws.append(Weather(date, week, weather))

ws.sort(key=lambda x : x.date)

for w in ws:
    if w.weather == 'Rain':
        print(w.date, w.week, w.weather)
        break