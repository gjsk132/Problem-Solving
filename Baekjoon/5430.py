# 백준 5430 : AC

# https://www.acmicpc.net/problem/5430

from collections import deque

input = open(0).readline

# R : 배열 뒤집기
# D : 첫 번째 요소 버리기 (error : empty array)

cases = int(input())

def answer():
    commands = input().strip()
    nums_len = int(input())
    nums = deque([])

    if nums_len:
       nums = deque(map(int, input().strip().lstrip("[").rstrip("]").split(",")))
    else:
        _ = input()

    left = True

    for c in commands:
        if c == "R":
            left ^= True
            continue
        
        if not nums_len:
            return "error"

        nums_len -= 1
        if left:
            nums.popleft()
        else:
            nums.pop()

    if left:
        return "["+",".join(map(str, nums))+"]"
    else:
        return "["+",".join(map(str, reversed(nums)))+"]"

for _ in range(cases):
    print(answer())