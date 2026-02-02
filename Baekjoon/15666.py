# 백준 15666 : N과 M (12)

# https://www.acmicpc.net/problem/15666

from collections import defaultdict

input = open("input.txt").readline

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))

stack = []

check = defaultdict(bool)

def recursion(pre, cnt):
    if cnt == M:
        answer = " ".join(map(str, stack))
        if not check[answer]:
            check[answer] = True
            print(answer) 
        return
    
    for i in range(pre, N):
        stack.append(nums[i])
        recursion(i, cnt+1)
        stack.pop()

recursion(0, 0)