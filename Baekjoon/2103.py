# 2103 : 직교다각형 복원
# https://www.acmicpc.net/problem/2103

from collections import defaultdict

point_cnt = int(input())

points_v = defaultdict(list)
points_h = defaultdict(list)

for _ in range(point_cnt):
    x, y = map(int, input().split())
    
    points_h[x].append(y)
    points_v[y].append(x)

length = 0

for _, values in points_h.items():
    values.sort()
    while values:
        length += values.pop() - values.pop()

for _, values in points_v.items():
    values.sort()
    while values:
        length += values.pop() - values.pop()

print(length)
