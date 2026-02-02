# 백준 6930 : Mod Inverse

# https://www.acmicpc.net/problem/6930

input = open("input.txt").readline

x, m = int(input()), int(input())

target = 1

while target < 100:
    if x*target%m == 1:
        break
    
    target += 1

if target == 100:
    print("No such integer exists.")
else:
    print(target)
