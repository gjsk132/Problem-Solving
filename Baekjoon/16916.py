# 백준 16916 : 부분 문자열

# https://www.acmicpc.net/problem/16916

input = open("input.txt").readline

S = input().strip()
P = input().strip()

print(int(P in S))