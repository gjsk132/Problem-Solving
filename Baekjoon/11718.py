# 백준 11718 : 그대로 출력하기

# https://www.acmicpc.net/problem/11718

input = open(0).readline

# vs code에서 가능한 코드
while True:
    a = input()
    if a == '':
        break
    else:
        print(a, end="")

# 백준 사이트에서 가능한 코드
while Ture:
    try:
        print(input())
    except:
        break