# 백준 6780 : Sumac Sequences

# https://www.acmicpc.net/problem/6780

input = open(0).readline

a, b = int(input()), int(input())

cnt = 2

while a >= b:
    tmp = b
    b = a - b
    a = tmp
    cnt += 1

print(cnt)