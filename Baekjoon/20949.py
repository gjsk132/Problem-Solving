# 백준 20949 : 효정과 새 모니터

# https://www.acmicpc.net/problem/20949

input = open("input.txt").readline

N = int(input())

monitors = [list(map(int, input().split()))+[i+1] for i in range(N)]

for m in sorted(monitors, key=lambda x: x[0]**2+x[1]**2, reverse=True):
    print(m[2])