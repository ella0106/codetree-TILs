def answer(arr):
    for elem in arr:
        # print('elem', elem)
        if elem % 2 == 0:
            print(elem // 2, end=' ')
        else:
            print(elem, end=' ')

n = input()
arr = list(map(int, input().split()))
answer(arr[:])