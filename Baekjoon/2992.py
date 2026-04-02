# 2992 : 크면서 작은 수
# https://www.acmicpc.net/problem/2992

from collections import defaultdict

num = input()
num_len = len(num)
num_count = defaultdict(int)

for n in num:
    num_count[n] += 1

flag = False

for now in range(int(num)+1, pow(10, num_len)):
    count = defaultdict(int)
    for n in str(now):
        count[n] += 1
    
    if num_count == count:
        print(now)
        flag = True
        break

if not flag:
    print(0)