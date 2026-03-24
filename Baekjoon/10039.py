# 10039 : 평균 점수
# https://www.acmicpc.net/problem/10039

print(sum([max(int(input()), 40) for _ in range(5)])//5)