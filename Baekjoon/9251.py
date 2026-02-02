# 백준 9251 : LCS

# https://www.acmicpc.net/problem/9251

input = open("input.txt").readline

a, b = input().strip(), input().strip()
board = [[0]*(len(b)+1) for _ in range(2)]

for i, ai in enumerate(a):
    for j, bj in enumerate(b):
        
        board[(i+1)%2][j+1] = max(board[i%2][j]+(1 if ai==bj else 0), board[(i+1)%2][j], board[i%2][j+1])

print(board[len(a)%2][len(b)])