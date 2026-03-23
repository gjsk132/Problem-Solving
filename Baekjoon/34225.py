# 34225 : 현대모비스 부품 조립
# https://www.acmicpc.net/problem/34225

input = open(0).readline

module_cnt = int(input())

modules = [(val, idx+1) for idx, val in enumerate(map(int, input().split()))]
modules.sort(key=lambda x: -x[0])

sums_m = [0]*module_cnt
sums_m[0] = modules[0][0]

max_value = 0

for i in range(1, module_cnt):
    sums_m[i] = modules[i][0] + sums_m[i-1]

for i in range(module_cnt):
    val = modules[0][0]+modules[i][0]+sums_m[i]
    if (val > max_value):
        max_value = val
        max_idx = i

answer = max_idx + 1

print(answer)
print(" ".join(map(str, sorted([idx for _, idx in modules[:answer]]))))