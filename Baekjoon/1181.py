# 백준 1181 : 단어 정렬

# https://www.acmicpc.net/problem/1181

# explain problem

input = open("input.txt").readline

N = int(input())

words = [input().strip() for _ in range(N)]

words = list(set(words))

words.sort()
print(words)
words.sort(key=len)

print("\n".join(words))