# 30618 : donstructive
# https://www.acmicpc.net/problem/30618

from collections import deque

n = int(input())

answer = deque([])

for i in range(n, 0, -1):
    if not (i%2):
        answer.appendleft(i)
    else:
        answer.append(i)

print(" ".join(map(str, answer)))