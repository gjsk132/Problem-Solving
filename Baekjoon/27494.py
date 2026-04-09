# 27494 : 2023년은 검은 토끼의 해
# https://www.acmicpc.net/problem/27494

N = int(input())

cnt = 0

def num_split(target: str, num:str):
    if not target in num:
        return False
    
    _, answer = num.split(target, 1)

    return answer

for n in range(1000, N+1):
    # _2_0_2_3_
    n = str(n)

    if not (n:= num_split("2", n)):
        continue
    
    if not (n:= num_split("0", n)):
        continue

    if not (n:= num_split("2", n)):
        continue

    if not "3" in n:
        continue

    cnt += 1

print(cnt)