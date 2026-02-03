#https://www.acmicpc.net/contest/problem/1615/5

input = open(0).readline

prob_cnt, left_time, target_score = map(int, input().split())

prob_info = []

# 입력 받으면서, 절대 못 푸는 문제 제거
for _ in range(prob_cnt):
    p_t, p_w = map(int,input().split())

    if p_t > left_time:
        prob_cnt -= 1
        continue
    
    prob_info.append((p_t, p_w))

# 풀 수 있는 문제 중 W점수 이상 받을 수 있는지 확인
# dp[선택 갯수][목표를 달성하기 위해 자야하는 시간] = W(w가 목표에 달성되었는지 이후 확인) ( 2500*2500 )
dp = [[0]*(left_time+1) for _ in range(prob_cnt)]

for _ in dp:
    print(_)