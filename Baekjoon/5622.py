# 백준 5622 : 다이얼

# https://www.acmicpc.net/problem/5622

input = open("input.txt").readline

word = input().strip()

word_num = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

sec = 0

for s in word:
    for idx, wn in enumerate(word_num):
        if s in wn:
            sec += idx + 3
            break

print(sec)