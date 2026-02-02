# 백준 34323 : 할인이 필요해

# https://www.acmicpc.net/problem/34323

input = open("input.txt").readline

N, M, price = map(int, input().split())

plus = M*price
sale = ((M+1)*(100-N)*price)//100

answer = min(plus, sale)

print(answer)