class Student:
    def __init__(self, h, w, n):
        self.h = h
        self.w = w
        self.n = n

N = int(input())
st_list = []
for i in range(N):
    h, w = tuple(map(int, input().split()))
    st_list.append(Student(h, w, i+1))

st_list.sort(key=lambda x : (x.h, x.w))
for st in st_list:
    print(st.h, st.w, st.n)