# 20502 : Gum색
# https://www.acmicpc.net/problem/20502

from collections import defaultdict

input = open(0).readline

N, M = map(int, input().split())

data = {idx : rank for idx, rank in enumerate(map(int, input().split()), start = 1)}

dic = defaultdict(list)

for idx in range(1, N+1):
    for keyword in list(map(int, input().split()))[1:]:
        dic[keyword].append(idx)

for _ in range(int(input())):
    kw = int(input())

    target = dic[kw]

    target.sort(key=lambda x: data[x])

    print(" ".join(map(str, target)) if target else -1)