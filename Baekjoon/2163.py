# 2163 : 초콜릿 자르기
# https://www.acmicpc.net/problem/2163

input = open(0).readline

N, M = map(int, input().split())

print(N-1 + N*(M-1))
