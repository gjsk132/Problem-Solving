# 백준 11004 : K번째 수

# https://www.acmicpc.net/problem/11004

input = open("input.txt").readline

N, target = map(int, input().split())

nums = sorted(list(map(int, input().split())))

print(nums[target-1])

