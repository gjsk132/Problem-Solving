# 백준 2908 : 상수

# https://www.acmicpc.net/problem/2908

input = open("input.txt").readline

A, B = input().split()

A, B = A[::-1], B[::-1]

print(A if int(A) > int(B) else B)