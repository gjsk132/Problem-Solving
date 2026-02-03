# 백준 16239 : Nadan

# https://www.acmicpc.net/problem/16239

input = open(0).readline

total = int(input())
cnt = int(input())

for i in range(cnt-1):
    print(i+1)
    total -= i+1

print(total)