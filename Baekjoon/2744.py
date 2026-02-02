# 백준 2744 : 대소문자 바꾸기

# https://www.acmicpc.net/problem/2744

input = open("input.txt").readline

words = input()

for w in words:
    if w.isupper():
        print(w.lower(), end = "")
    else:
        print(w.upper(), end = "")

