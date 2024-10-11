a_len, b_len = tuple(map(int, input().split()))
a = input().split()
b = input().split()

def is_same(a_len, b_len, a, b):
    for i in range(a_len):
        
        # print(a[i], b[0])
        if a[i] == b[0]:
            # print(a[i:i+b_len-1])
            if a[i:i+b_len-1] == b[:b_len-1]:
                return 'Yes'
    return 'No'

print(is_same(a_len, b_len, a, b))