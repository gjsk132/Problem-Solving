#https://www.acmicpc.net/contest/problem/1615/1

input = open(0).readline

n_h, n_min, n_sec = map(int, input().split(":"))
s_h, s_min, s_sec = map(int, input().split(":"))

t, k = map(int, input().split())

now = n_sec + n_min*60 + n_h*60*60
start = s_sec + s_min*60 + s_h*60*60

left = start-now

if left < 0:
    print(0)
else:
    limit = t*(100-k)//100

    if limit > left:
        print(0)
    else:
        print(1)