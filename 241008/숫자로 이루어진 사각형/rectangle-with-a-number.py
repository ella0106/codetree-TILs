def p(n):
    num = '1 2 3 4 5 6 7 8 9 '
    m = n*n // 9
    r = n*n % 9
    result = num * m + num[:r*2]
    for i in range(n):
        print(result[2*n*i:2*n*(i+1)])
        

p(int(input()))