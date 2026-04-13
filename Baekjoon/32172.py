# 32172 : 현권이와 신기한 수열
# https://www.acmicpc.net/problem/32172

from collections import defaultdict

idx = int(input())

A_check = defaultdict(bool)
A = 0

for i in range(idx+1):
    tmp = A-i
    if tmp < 0 or A_check[tmp]:
        A = A+i
    else:
        A = A-i
    
    A_check[A] = True

print(A)
