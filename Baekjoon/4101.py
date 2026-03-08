# 4101 : 크냐?
# https://www.acmicpc.net/problem/4101

while True:
    a, b = map(int, input().split())
    if not a and not b:
        break
       
    if a > b:
        print("Yes")
    else:
        print("No")