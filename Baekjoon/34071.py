# 백준 34071 : 첫 번째 문제는 정말 쉬운 문제일까?

# https://www.acmicpc.net/problem/34071

input = open(0).readline

n = int(input())

scores = [int(input()) for _ in range(n)]
first = scores[0]

if min(scores) == first:
    print("ez")
elif max(scores) == first:
    print("hard")
else:
    print("?")