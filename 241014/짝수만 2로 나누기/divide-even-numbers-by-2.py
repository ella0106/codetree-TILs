def answer(arr):
    for elem in arr:
        # print('elem', elem)
        e = int(elem)
        if e % 2 == 0:
            print(e // 2, end=' ')
        else:
            print(e, end=' ')

n = input()
arr = input().split(' ')
answer(arr[:])