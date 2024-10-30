class Person:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

n = int(input())
people = []

for _ in range(n):
    name, addr, city = tuple(input().split())
    people.append(Person(name, addr, city))


people.sort(key=lambda x : x.name)
p = people[-1]

print('name {}'.format(p.name))
print('addr {}'.format(p.addr))
print('city {}'.format(p.city))