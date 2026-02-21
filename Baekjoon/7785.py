# 7785 : 회사에 있는 사람
# https://www.acmicpc.net/problem/7785

input = open(0).readline

orders = int(input())

people = {}

for _ in range(orders):
    name, log = input().split()

    if log == "enter":
        people[name] = True
    
    else:
        people[name] = False

left_people = []

for p, isleft in people.items():
    if isleft:
        left_people.append(p)

print("\n".join(list(reversed(sorted((left_people))))))