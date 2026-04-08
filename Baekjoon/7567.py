# 7567 : 그릇
# https://www.acmicpc.net/problem/7567

plates = input()

height = 10

for i in range(1, len(plates)):
    height += (5 if plates[i] == plates[i-1] else 10)

print(height)