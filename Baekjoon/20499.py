# 20499 : Darius님 한타 안 함?
# https://www.acmicpc.net/problem/20499

input = open(0).readline

kill, death, assist = map(int, input().split("/"))

print("hasu" if kill+assist<death or death==0 else "gosu")