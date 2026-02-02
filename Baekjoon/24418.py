# 백준 24418 : 알고리즘 수업 - 행렬 경로 문제 1

# https://www.acmicpc.net/problem/24418

input = open("input.txt").readline

n = int(input())

m = [list(map(int, input().split())) for _ in range(n)]

board = [[0]*(n+1) for i in range(n+1)]

board[0] = [0] + [1]*n

for i in range(n):
    board[i+1][0] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        board[i][j] = board[i-1][j] + board[i][j-1]

print(board[n][n], end=" ")
print(n*n)