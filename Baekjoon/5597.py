# 백준 5597 : 과제 안 내신 분..?

# https://www.acmicpc.net/problem/5597

# explain problem

input = open(0).readline

check = [0 for _ in range(31)]

for i in range(28):
    check[int(input())] = 1

for k, v in enumerate(check[1:]):
    if v == 0:
        print(k+1)