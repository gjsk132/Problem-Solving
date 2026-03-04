# 26040 : 특정 대문자를 소문자로 바꾸기
# https://www.acmicpc.net/submit/26040/103494566

input = open(0).readline

sentence = input().strip()
lower_alpha = list(input().split())

for la in lower_alpha:
    sentence = sentence.replace(la, la.lower())
    
print(sentence)