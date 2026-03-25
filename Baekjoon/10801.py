# 10801 : 카드게임
# https://www.acmicpc.net/problem/10801

A_win, B_win = 0, 0

for A, B in zip(map(int, input().split()), map(int, input().split())):
    
    if A > B:
        A_win += 1
    elif A is not B:
        B_win += 1
    
if A_win > B_win:
    print("A")
elif B_win > A_win:
    print("B")
else:
    print("D")