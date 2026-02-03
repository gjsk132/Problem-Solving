#https://www.acmicpc.net/contest/problem/1615/2

from collections import defaultdict

input = open(0).readline

width, height = map(int, input().split())

loto = [input().strip() for _ in range(height)]

length = int(input())

loto_result = defaultdict(int)

for l in loto:
    for i in range(0, width-length+1):
        loto_result[l[i:i+length]] += 1

print(max(loto_result.values()))