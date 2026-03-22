# 10817 : 세 수
# https://www.acmicpc.net/problem/10817

a, b, c = map(int, input().split())

print(a+b+c-max(a,b,c)-min(a,b,c))