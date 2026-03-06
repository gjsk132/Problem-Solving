# 34028 : 우리의 다정한 계절 속에(Seasons of Memories)
# https://www.acmicpc.net/problem/34028

input = open(0).readline

y, m, d = map(int, input().split())

sy, sm, sd = 2015, 1, 16

answer = (y - sy)*4 + 1

if m > 11:
    answer += 4
elif m > 8:
    answer += 3
elif m > 5:
    answer += 2
elif m > 2:
    answer += 1

print(answer)