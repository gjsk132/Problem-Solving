# 1159 : 농구 경기
# https://www.acmicpc.net/problem/1159

from collections import defaultdict

input = open(0).readline

people = int(input())
players = [input().strip() for _ in range(people)]

first_name = defaultdict(int)

for p in players:
    first_name[p[0]] += 1

answers = []

for fn, cnt in first_name.items():
    if cnt >= 5:
        answers.append(fn)
    
if len(answers):
    print("".join(map(str, sorted(answers))))
else:
    print("PREDAJA")