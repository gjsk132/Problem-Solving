from collections import OrderedDict


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    # OrderedDict로 선언
    cache = OrderedDict()
    total = 0

    for city in cities:
        city = city.lower()

        if city in cache:  # 조회 O(1)
            cache.move_to_end(city)  # 최근 사용 처리 O(1)
            total += 1
        else:
            if len(cache) == cacheSize:
                cache.popitem(last=False)  # 가장 오래된 값 제거 O(1)
            cache[city] = True
            total += 5

    return total
