# 10241 : Baseball
# https://www.acmicpc.net/problem/10214

cases = int(input())

def result():
    y, k = 0, 0

    for _ in range(9):
        a, b = map(int, input().split())
        y += a
        k += b

    if y > k:
        print("Yonsei")
    elif y < k:
        print("Korea")
    else:
        print("Draw")

for _ in range(cases):
    result()