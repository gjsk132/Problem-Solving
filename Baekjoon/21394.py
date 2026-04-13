# 21394 : 숫자 카드
# https://www.acmicpc.net/problem/21394

input = open(0).readline

def list_numbers():
    nums = [0]+list(map(int, input().split()))
    nums[9], nums[6] = nums[9] + nums[6], 0

    ans = ""

    is_left = True

    for n, cnt in enumerate(nums):
        if cnt == 0:
            continue
        
        half_cnt = cnt//2
        str_n = str(n)

        if cnt%2 and is_left: # 홀수 + 왼쪽
            ans = str_n*(half_cnt+1) + ans + str_n*half_cnt
            is_left = False
        elif cnt%2 and not is_left: # 홀수 + 오른쪽
            ans = str_n*half_cnt + ans + str_n*(half_cnt+1)
            is_left = True
        else: # 짝수
            ans = str_n*half_cnt + ans + str_n*half_cnt

    return ans if not is_left else reversed(ans)

cases = int(input())

for _ in range(cases):
    print(" ".join(list_numbers()))

