# 백준 2257 : 화학식량

# https://www.acmicpc.net/problem/2257

input = open("input.txt").readline

elements = input().strip()

value = {
    "H" : 1,
    "C" : 12,
    "O" : 16,
    "(" : 0
}

stack = []

for i in range(len(elements)):
    e = elements[i]
    
    if e.isdigit():
        stack.append(stack.pop()*int(e))

    elif not e == ")":
        stack.append(value[e])
    else:
        while stack:
            if (a:=stack.pop()) == 0:
                break
            elif (b:=stack.pop()) == 0:
                stack.append(a)
                break

            else:
                stack.append(a+b)
print(sum(stack))