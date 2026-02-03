# 백준 31908 : 커플링 매치

# https://www.acmicpc.net/problem/31908

from collections import defaultdict

input = open(0).readline

cnt = int(input())

couples = defaultdict(list)

for _ in range(cnt):
    name, ring = input().split()

    if ring == "-":
        continue

    couples[ring].append(name)

answer = []

for ring, name in couples.items():
    same_ring_cnt = len(name)

    if same_ring_cnt == 2:
        answer.append(" ".join(name))

print(len(answer))
for a in answer:
    print(a)