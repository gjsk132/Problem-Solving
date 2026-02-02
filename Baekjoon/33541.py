# 백준 33541 : 2025는 무엇이 특별할까?

# https://www.acmicpc.net/problem/33541

input = open(0).readline

limit = 10000

now = int(input()) + 1

while now < limit:
    a, b = now//100, now%100
    if now == pow(a+b, 2):
        print(now)
        break
    
    now += 1

if now == 10000:
    print(-1)
