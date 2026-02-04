# 4999 :  아!
# https://www.acmicpc.net/problem/4999

input = open(0).readline

limit = input().strip().count('a')
request = input().strip().count('a')

print("no" if request > limit else "go")