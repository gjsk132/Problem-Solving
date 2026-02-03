# 백준 9012 : 괄호

# https://www.acmicpc.net/problem/9012

input = open(0).readline

def check_VPS(PS):
    while "()" in PS:
        PS = PS.replace("()", "")
    
    if PS == "":
        return True
    else:
        return False

N = int(input())

# for _ in range(N):
#    now_PS = input().strip()
#
#    if check_VPS(now_PS):
#        print("YES")
#    else:
#        print("NO")

for _ in range(N):
    now_PS = input().strip()

    left = 0

    for i in now_PS:
        if i == "(":
            left += 1
        else:
            left -= 1

        if left < 0:
            break

    if not left == 0:
        print("NO")
    else:
        print("YES")
    
