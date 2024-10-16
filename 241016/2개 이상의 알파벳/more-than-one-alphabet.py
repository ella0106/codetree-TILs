s = input()
s_list = []
for i in range(len(s)):
    s_list.append(s[i])
s_list = set(s_list)

if len(s_list) >= 2:
    print('Yes')
else:
    print('No')