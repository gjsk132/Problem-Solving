cases = int(input()) 
for _ in range(cases):
    value = [(input().split()) for _ in range(int(input()))]
    value.sort(key=lambda x: -int(x[1]))
    print(value[0][0])