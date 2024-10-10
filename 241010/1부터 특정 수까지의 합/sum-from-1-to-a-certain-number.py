def func(n):
    const = 0
    for i in range(1, n+1):
        const += i
    return const // 10

print(func(int(input())))