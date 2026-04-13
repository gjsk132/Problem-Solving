# 10103 : 주사위 게임
# https://www.acmicpc.net/problem/10103

rounds = int(input())

p1, p2 = 100, 100

for _ in range(rounds):
    dice1, dice2 = map(int, input().split())

    if dice1 > dice2:
        p2 -= dice1
    elif dice1 < dice2:
        p1 -= dice2

print(p1)
print(p2)