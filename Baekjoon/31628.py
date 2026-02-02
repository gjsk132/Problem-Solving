# 백준 31628 : 가지 한 두름 주세요

# https://www.acmicpc.net/problem/31628

input = open("input.txt").readline

cols = [set([]) for _ in range(10)]

flag = False

for _ in range(10):
    tmp = list(input().split())

    if len(set(tmp)) == 1:
        flag = True
        break
    
    for idx, c in enumerate(tmp):
        cols[idx].add(c)
    
if not flag:
    for c in cols:
        if len(c) == 1:
            flag = True

print(1 if flag else 0)
