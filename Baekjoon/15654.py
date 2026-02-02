# 백준 15654 : N과 M (5)

# https://www.acmicpc.net/problem/15654

input = open("input.txt").readline

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))

check = [False]*N
stack = []

def recursion(cnt):
    if cnt == M:
        print(" ".join(map(str, stack)))
        return
    
    for i in range(N):
        if check[i]:
            continue

        stack.append(nums[i])
        check[i] = True

        recursion(cnt+1)
        
        stack.pop()
        check[i] = False

recursion(0)
