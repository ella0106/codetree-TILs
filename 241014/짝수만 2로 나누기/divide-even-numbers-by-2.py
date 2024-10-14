def answer(arr):
    for elem in arr:
        if int(elem) % 2 == 0:
            print(int(elem) // 2, end=' ')
        else:
            print(elem, end=' ')

n = input()
arr = input().split(' ')
answer(arr[:])