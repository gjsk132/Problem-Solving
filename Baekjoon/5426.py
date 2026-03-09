# 5426 : 비밀 편지
# https://www.acmicpc.net/problem/5426
from math import sqrt

input = open(0).readline

cases = int(input())

def decoding(s):
    size = int(sqrt(len(s)))

    for i in range(1, size+1):
        for j in range(size):
            print(s[(j*size)+(size-i)], end="")

    print()

for _ in range(cases):
    decoding(input().strip())

    
