# 백준 1923 : 정수 삼각형

# https://www.acmicpc.net/problem/1926

input = open("input.txt").readline

size = int(input())

board = [list(map(int, input().split()))+[0]*(size-i-1) for i in range(size)]

for floor in range(size):
    if floor == 0:
        continue

    for idx in range(size):
        if idx > floor:
            continue
        
        board[floor][idx] += max(0 if idx > floor else board[floor-1][idx-1],board[floor-1][idx])

print(max(board[-1]))