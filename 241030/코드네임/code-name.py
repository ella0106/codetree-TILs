class Person:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
people = []
for _ in range(5):
    name, score = tuple(input().split())
    people.append(Person(name, int(score)))

people.sort(key=lambda x:x.score)
people1 = people[0]

print(people1.name, people1.score)