# 백준 2929 : 머신 코드

# https://www.acmicpc.net/problem/2929

input = open("input.txt").readline

contents = input().strip()

pos = 0

NOP = 0

for c in list(contents):
    while c.isupper() and pos%4:
        NOP += 1
        pos += 1
    pos += 1

print(NOP)