# 4740 : 거울, 오!거울
# https://www.acmicpc.net/problem/4740

answer = []

while True:
    sentence = input()

    if sentence == '***':
        break

    print(sentence[::-1])