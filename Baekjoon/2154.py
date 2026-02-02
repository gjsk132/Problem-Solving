# 백준 2154 : 수 이어 쓰기 2

# https://www.acmicpc.net/problem/2154

input = open(0).readline

num = input().strip()

nums = "".join(str(i) for i in range(1, int(num)+1))

print(nums.index(num)+1)