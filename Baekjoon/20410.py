# 백준 20410 : 추첨상 사수 대작전! (Easy)

# https://www.acmicpc.net/problem/20410

input = open("input.txt").readline

m, seed, x_1, x_2 = map(int, input().split())

flag = False

for a in range(m):
    if flag:
        break
    for c in range(m):
        if x_1 == (a*seed+c)%m and x_2 ==(a*x_1+c)%m:
            flag = True
            print(a, c)
            break