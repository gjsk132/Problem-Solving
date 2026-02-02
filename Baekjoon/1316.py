# 백준 1316 : 그룹 단어 체커

# https://www.acmicpc.net/problem/1316

from collections import defaultdict

input = open("input.txt").readline

answer = 0

words = int(input())

def group_checker(w):
    alpha = defaultdict(bool)

    now = ""

    for a in list(w):
        if a == now:
            continue
        else:
            if alpha[a]:
                return False
            alpha[a] = True

            now = a

    return True

for _ in range(words):
    if group_checker(input().strip()):
        answer += 1

print(answer)