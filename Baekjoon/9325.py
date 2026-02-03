# 백준 9325 : 얼마?

# https://www.acmicpc.net/problem/9325

input = open(0).readline

cases = int(input())

for _ in range(cases):
    car_price = int(input())
    options_cnt = int(input())

    for _ in range(options_cnt):
        o_cnt, o_price = map(int, input().split())

        car_price += o_cnt * o_price
    
    print(car_price)