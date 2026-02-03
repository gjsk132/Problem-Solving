# 백준 10813 : 공 바꾸기

# https://www.acmicpc.net/problem/10813

input = open(0).readline

N, M = map(int, input().split())

nums = [i+1 for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())

    tmp = nums[b-1]
    nums[b-1] = nums[a-1]
    nums[a-1] = tmp

print(" ".join(map(str, nums)))