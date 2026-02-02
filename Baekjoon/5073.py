# 백준 5073 : 삼각형과 세 변

# https://www.acmicpc.net/problem/5073

input = open("input.txt").readline

while True:
    a, b, c = map(int, input().split())

    if not a or not b or not c:
        break
    
    max_n = max(a, b, c)

    if max_n >= a+b+c-max_n:
        print("Invalid")
        continue
    
    kinds = len(set([a, b, c]))

    if kinds == 3:
        print("Scalene")
    elif kinds == 2:
        print("Isosceles")
    else:
        print("Equilateral")