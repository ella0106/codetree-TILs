sic = input()
a, suffix, b = sic.split()
a, b = int(a), int(b)
def add(a, b):
    return a+b
def diff(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a // b

if suffix == '+':
    print(sic, '=', add(a,b))
if suffix == '-':
    print(sic, '=', diff(a,b))
if suffix == '/':
    print(sic, '=', div(a,b))
if suffix == '*':
    print(sic, '=', mul(a,b))
else:
    print(False)