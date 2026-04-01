# 10798 : 세로읽기
# https://www.acmicpc.net/problem/10798

words = [input() for _ in range(5)]

for col in range(max([len(words[idx]) for idx in range(5)])):
    for row in range(5):
        if col >= len(words[row]):
            continue
        print(words[row][col], end="")