# 백준 11650 : 좌표 정렬하기

# https://www.acmicpc.net/problem/11650

input = open(0).readline

N = int(input())
dots = [list(map(int, input().split())) for _ in range(N)]

dots.sort(key = lambda x: (x[0], x[1]))

for d in dots:
    print(d[0], d[1])
