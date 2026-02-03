# 백준 31880 : K512컵 개최!

# https://www.acmicpc.net/problem/31880

input = open(0).readline

n, m = map(int, input().split())

n_sum = sum(list(map(int, input().split())))

answer = n_sum

for m_e in map(int, input().split()):
    if not m_e:
        continue
    answer *= m_e

print(answer)