# 백준 14626 : ISBN

# https://www.acmicpc.net/problem/14626

# explain problem

input = open("input.txt").readline

ISBN = input().strip()

total = 0
lost_pos = 0

for idx, num in enumerate(ISBN):
    if num == "*":
        lost_pos = idx
        continue

    n = int(num)
    
    if idx%2:
        total += 3*n
    else:
        total += n


lost = (10 - total%10)%10

if lost_pos%2:
    while lost%3:
        lost += 10
    lost //= 3

print(lost)