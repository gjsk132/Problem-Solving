# 2183 : 테니스 시합
# https://www.acmicpc.net/problem/2183

# 결국 마지막 경기를 이기는 사람이 우승 조건을 만족하고 경기가 끝난 것

input = open(0).readline

people_cnt, win_people = input().split()

print(win_people[-1])