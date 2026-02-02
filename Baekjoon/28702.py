# 백준 28702 : FizzBuzz

# https://www.acmicpc.net/problem/28702

# explain problem

input = open("input.txt").readline

# 주어진 3개의 문자열이 전부 숫자가 아닐 경우는 없음
# 숫자인 것을 찾아서 다음에 올 숫자 찾기
# 나누어서 출력해야할 값 구하기

target = 0
gap = 3

for _ in range(3):
    tmp = input().strip()

    try:
        tmp = int(tmp)
        target = gap + tmp
        break
    except:
        gap -= 1

answer = ""

if target%3 == 0:
    answer += "Fizz"
if target%5 == 0:
    answer += "Buzz"

print(target if answer == "" else answer)

