# 10994 : 별 찍기 - 19
# https://www.acmicpc.net/problem/10994

input = open(0).readline

size = int(input())

stars = ['*']

for i in range(size-1):
    stars = [' '*(4*(i+1)-1)]+[' '+i+' ' for i in stars]+[' '*(4*(i+1)-1)]

    stars = ['*'+i+'*' for i in stars]

    stars = ['*'*len(stars[0])] + stars + ['*'*len(stars[0])]

print("\n".join(stars))