# 15821 : 낚이고 낚아라
# https://www.acmicpc.net/problem/15821

from heapq import *

input = open(0).readline

# 각 도형에서 가장 멀리 있는 점을 구해서 heapq에 넣기
# heapq에서 하나씩 빼기

fishing_spot_cnt, need_spot_cnt = map(int, input().split())

# 다각형 점들 중 가장 먼 거리 반환
def find_furthest_distance():
    points = list(map(int, input().split()))

    furthest_distance = 0

    while points:
        y, x = points.pop(), points.pop()

        furthest_distance = max(furthest_distance, round(pow(x,2)+pow(y,2), 2))

    return furthest_distance

furthest_distances_of_fishing_spot = []

# 각 도형의 가장 먼 거리를 heap에 저장
for _ in range(fishing_spot_cnt):
    spot_points_cnt = int(input())
    heappush(furthest_distances_of_fishing_spot, find_furthest_distance())

# 원하는 수에 맞게 하나씩 pop

valid_spot_cnt = 0

while valid_spot_cnt < need_spot_cnt:
    valid_spot_cnt += 1
    target_distance = heappop(furthest_distances_of_fishing_spot)

print(f"{target_distance:0.2f}")