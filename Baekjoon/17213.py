# 17213 : 과일 서리
# https://www.acmicpc.net/problem/17213

input = open(0).readline

N, M = int(input()), int(input())

def backtracking(pos, left):
    cnt = 0

    # base
    if pos == N:
        return 1

    # recursion
    for i in range(0, left+1):
        cnt += backtracking(pos+1, left-i)
    
    return cnt

print(backtracking(1, M-N))