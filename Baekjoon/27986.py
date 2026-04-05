# 27986 : 평범한 구성적 문제
# https://www.acmicpc.net/problem/27986

X_length, section_cnt = map(int, input().split())

shortest_section_len = float('inf')

X = [0]*(X_length +1)

sections = [tuple(map(int, input().split())) for _ in range(section_cnt)]
sections.sort(key=lambda x : x[1]-x[0]+1)

K = sections[0][1]-sections[0][0]+1

for section in sections:
    check = [False]*(K+1)
    for num in X[section[0]:section[1]+1]:
        check[num] = True
    
    num = 1

    for idx in range(section[0], section[1]+1):
        if not X[idx] == 0:
            continue

        if num > K:
            break
        
        X[idx] = num
        check[num] = True

        while num <= K and check[num]:
            num += 1

for idx, val in enumerate(X):
    if val == 0:
        X[idx] = 1

print(" ".join(map(str, X[1:])))