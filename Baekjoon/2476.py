# 2476 : 주사위 게임
# https://www.acmicpc.net/problem/2476

input = open(0).readline

people = int(input())

max_price = 0

for _ in range(people):
    a, b, c = map(int, input().split())

    if (a == b and b == c):
        max_price = max(max_price, 10000+a*1000)
    elif (a == b or b == c or a == c):
        max_price = max(max_price, 1000+(a+b+c-sum({a, b, c}))*100)
    else:
        max_price = max(max_price, max(a, b, c)*100)

print(max_price)