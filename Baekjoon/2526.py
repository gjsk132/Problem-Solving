# 2526 : 싸이클
# https://www.acmicpc.net/problem/2526

from collections import defaultdict

input = open(0).readline

N, P = map(int, input().split())

nums_pos = defaultdict(int)
nums_pos[N] = 1

next_num = N*N%P
last = 1

while nums_pos[next_num] == 0:
    last += 1
    nums_pos[next_num] = last

    next_num = (next_num*N)%P

print(last - nums_pos[next_num] + 1) 
