# 1789 : 수들의 합
# https://www.acmicpc.net/problem/1789

S = int(input())

cnt = 1

total = 0

while total + cnt <= S:
    total += cnt
    cnt += 1

print(cnt-1)
