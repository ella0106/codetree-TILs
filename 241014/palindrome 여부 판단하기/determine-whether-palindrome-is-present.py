def string(s):
    if s == s[::-1]:
        print('Yes')
    else:
        print('No')

s = input()
string(s)