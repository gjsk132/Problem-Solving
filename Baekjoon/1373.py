# 1373 : 2진수 8진수
# https://www.acmicpc.net/problem/1373

input = open(0).readline

num_two = "0b"+input().strip()

print(oct(int(num_two, 2))[2:])