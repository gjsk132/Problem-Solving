# 1225 : 이상한 곱셈
# https://www.acmicpc.net/problem/1225

input = open(0).readline

A, B = input().split()

print(sum(map(int, list(A)))*sum(map(int, list(B))))