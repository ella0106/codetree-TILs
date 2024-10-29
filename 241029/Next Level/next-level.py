class person:
    def __init__(self, user, lv):
        self.user = user
        self.lv = lv

a = person('codetree', 10)
print('user {} lv {}'.format(a.user, a.lv))
u, l = tuple(input().split())
p = person(u, int(l))

print('user {} lv {}'.format(p.user, p.lv))