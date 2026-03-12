# 34687 : 라면 끓여 먹자 야호
# https://www.acmicpc.net/problem/34687

input = open(0).readline

N, M = map(int, input().split())

print("yaho" if M*100 >= N*81 else "no")