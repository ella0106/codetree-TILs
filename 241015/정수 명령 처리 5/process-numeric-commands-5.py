n = int(input())
l = []
for i in range(n):
    s = input()
    if s == 'size':
        print(len(l))
    elif s == 'pop_back':
        l.pop()
    else:
        s, num = s.split()
        num = int(num)
        if s == 'push_back':
            l.append(num)
        if s == 'get':
            print(l[num-1])