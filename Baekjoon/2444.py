# 백준 2444 : 별 찍기 - 7

# https://www.acmicpc.net/problem/2444

input = open(0).readline

cnt = int(input())

tmp = [2*i+1 for i in range(cnt)]

for i in range(cnt):
    print(" "*(cnt-i-1)+"*"*tmp[i])

for i in range(cnt-2,-1,-1):
    print(" "*(cnt-i-1)+"*"*tmp[i])