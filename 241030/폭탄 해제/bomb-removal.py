class P:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second
    
code, color, second = tuple(input().split())
a = P(code, color, second)

print('code : {}'.format(a.code))
print('color : {}'.format(a.color))
print('second : {}'.format(a.second))