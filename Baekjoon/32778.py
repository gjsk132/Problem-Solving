# 32778 : 가희와 부역명
# https://www.acmicpc.net/problem/32778

input = open(0).readline

tmp = input().strip()

if "(" in tmp:
    print("\n".join(tmp[:-1].split(" (")))
else:
    print(tmp)
    print("-")