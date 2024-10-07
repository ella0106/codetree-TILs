import sys
n = int(input())
people = input().split()

max_sum = sys.maxsize
for i in range(n):
    sum_diff = 0
    for j in range(n):
        sum_diff += abs(j-i) * int(people[j])

    max_sum = min(max_sum, sum_diff)

print(max_sum)