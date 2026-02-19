# 25576 : 찾았다 악질
# https://www.acmicpc.net/problem/25576

input = open(0).readline

N, M = map(int, input().split())

std = list(map(int, input().split()))

board = [list(map(int,input().split())) for _ in range(N-1)]

bad_cnt = 0

for b in board:
    tmp = sum([abs(std[i]-b[i]) for i in range(M)])

    if tmp > 2000:
        bad_cnt += 1

print("YES" if bad_cnt*2 >= N else "NO")