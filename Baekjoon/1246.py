# 백준 1246 : 온라인 판매

# https://www.acmicpc.net/problem/1246

input = open("input.txt").readline

N, M = map(int, input().split())

prices = sorted([int(input()) for _ in range(M)])

p = 0
t = 0

for i, price in enumerate(prices):
    cnt = min(N, M-i)

    if price*cnt > t:
        p = price
        t = price*cnt

print(p, t)