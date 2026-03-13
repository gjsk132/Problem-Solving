# 5717 : 상근이와 친구들
# https://www.acmicpc.net/problem/5717

input = open(0).readline

while(True):
    n, m = map(int, input().split())
    if (not (total := n + m)):
        break
    else:
        print(total)