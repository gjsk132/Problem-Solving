# 16918 : 봄버맨
# https://www.acmicpc.net/problem/16918

# 짝수일 때는 동일하게 all_bomb
# 홀수일 때는 bomb이 터지고 남은 위치만 계속 남음

R, C, target_time = map(int, input().split())

offset = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]

all_bomb = ['O'*C for _ in range(R)]
now_board = [input() for _ in range(R)]

def next_baord_state(n_board):

    next_board = [['O']*C for _ in range(R)]
    
    for row, val in enumerate(n_board):
        for col, e in enumerate(val):
            if e == '.':
                continue
            
            for px, py in offset:
                nx, ny = row + px, col + py

                if nx < 0 or nx == R or ny < 0 or ny == C:
                    continue

                next_board[nx][ny] = '.'

    return next_board

if target_time%2:
    for _ in range(target_time//2):
        now_board = next_board_state(now_board)
    
    for row in now_board:
        print("".join(row))
    
else:
    for row in all_bomb:
        print("".join(row))