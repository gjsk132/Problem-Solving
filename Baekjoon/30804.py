# 백준 30804 : 과일 탕후루

# https://www.acmicpc.net/problem/30804

# 앞뒤에 몇 개를 빼는지는 딱히 중요하지 않음
# 그냥 하나씩 나아가면서, 2종류 이상 나오게 되면, 전환하는 방식

# 같은게 연속으로 몇 개 나왔는지, 숫자가 변경될 때, 이전에 나왔던거랑 같은지 확인하기

input = open("input.txt").readline

N = int(input())
fruits = list(map(int,input().split()))

def calculate_answer():
    pre, now = 0, fruits[0]

    pre_length, now_length = 0, 1

    answer = 0

    for f in fruits[1:]:
        if now == f:
            now_length += 1
            continue

        if pre == f:
            pre, now = now, f
            pre_length, now_length = pre_length + now_length, 1
            continue
        
        answer = max(answer, pre_length + now_length)
        pre, now = now, f
        pre_length, now_length = now_length, 1

    answer = max(answer, pre_length + now_length)

    return answer

if N <= 2:
    print(N)
else:
    print(calculate_answer())