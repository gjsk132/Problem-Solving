# 1212 : 8진수 2진수
# https://www.acmicpc.net/problem/1212

input = open(0).readline

num_eight = "0o"+input().strip()

print(bin(int(num_eight, 8))[2:])