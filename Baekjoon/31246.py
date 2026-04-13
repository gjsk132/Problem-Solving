# 31246 : 모바일 광고 입찰
# https://www.acmicpc.net/problem/31246

from heapq import *
from collections import defaultdict

total_cnt, target_cnt = map(int, input().split())

satisfied_cnt = 0

bid_cnt = defaultdict(int)
amount_required_to_bid = []

for _ in range(total_cnt):
    moloco_price, max_price = map(int, input().split())

    if moloco_price < max_price:
        bid = max_price-moloco_price
        if not bid_cnt[bid]:
            heappush(amount_required_to_bid, max_price-moloco_price)
        bid_cnt[bid] += 1
    else:
        satisfied_cnt += 1

need_price = 0

while satisfied_cnt < target_cnt:
    need_price = heappop(amount_required_to_bid)
    satisfied_cnt += bid_cnt[need_price]

print(need_price)