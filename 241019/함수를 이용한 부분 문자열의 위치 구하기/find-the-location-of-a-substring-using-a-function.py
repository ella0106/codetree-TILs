n = input()
m = input()

m_num = len(m)
def answer():
    for i in range(len(n) - m_num + 1):
        # print(n[i:i + m_num])
        if n[i:i + m_num] == m:
            return print(i)
    return print(-1)

answer()