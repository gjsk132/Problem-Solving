# 백준 31403 : A + B - C

# https://www.acmicpc.net/problem/31403

input = open("input.txt").readline

a, b, c = (int(input()) for _ in range(3))

print(a+b-c)
print(int(str(a)+str(b))-c)