class seven:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

c, p, t = input().split()
s = seven(c, p, t)
print('secret code : {}'.format(s.code))
print('meeting point : {}'.format(s.place))
print('time : {}'.format(s.time))