# 9414 : 프로그래밍 대회 전용 부지
# https://www.acmicpc.net/problem/9414

from heapq import *

limit = 5*pow(10, 6)

input = open(0).readline

def calculate_need_money():
    costs = []

    while (now := int(input())):
        costs.append(now)

    costs = sorted(costs, key=lambda x: -x)

    need_money = 0

    for idx, cost in enumerate(costs):
        if (need_money := need_money + 2*pow(cost, idx+1)) > limit:
            return "Too expensive"

    return need_money

cases = int(input())

for _ in range(cases):
    print(calculate_need_money())