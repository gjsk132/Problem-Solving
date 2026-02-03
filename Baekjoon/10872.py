# 백준 10872 : 팩토리얼

# https://www.acmicpc.net/problem/10872

# 단순 팩토리얼 구현 문제

input = open(0).readline

cnt = int(input())

answer = 1

for i in range(2, cnt+1):
    answer *= i

print(answer)
