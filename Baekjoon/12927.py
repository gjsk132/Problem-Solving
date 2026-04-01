# 12927 : 배수 스위치
# https://www.acmicpc.net/problem/12927

state = input()
push_cnt = 0

state_list = [1 if idx == "Y" else 0 for idx in state]

for pos in range(len(state)//2):
    if not state_list[pos]:
        continue
    
    push_cnt += 1

    for click_pos in range(pos, len(state), pos+1):
        state_list[click_pos] ^= 1

print(push_cnt + sum(state_list))