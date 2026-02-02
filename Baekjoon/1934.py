# 백준 1934 : 최소공배수

# https://www.acmicpc.net/problem/1934

input = open("input.txt").readline

cases = int(input())

for _ in range(cases):
    a, b = map(int, input().split())

    max_n, min_n = max(a, b), min(a, b)

    while (remain:=max_n%min_n):
        max_n, min_n = min_n, remain
    
    gcd = min_n

    print(a*b//gcd)
