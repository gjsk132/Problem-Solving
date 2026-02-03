# 백준 21567 : 숫자의 개수 2

# https://www.acmicpc.net/problem/21567

input = open(0).readline

A = int(input())
B = int(input())
C = int(input())

cal = A * B * C

nums = [0 for _ in range(10)]

for n in str(cal):
    nums[int(n)] += 1

for n in nums:
    print(n)