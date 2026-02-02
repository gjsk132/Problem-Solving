# 백준 10773 : 제로

# https://www.acmicpc.net/problem/10773

input = open("input.txt").readline

K = int(input())

moneys = []

for _ in range(K):
    m = int(input())

    if m == 0:
        moneys.pop()
    else:
        moneys.append(m)

print(sum(moneys))