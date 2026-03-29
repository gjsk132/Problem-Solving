# 10886 : 0 = not cute / 1 = cute

ans = [0, 0]
for _ in range(int(input())):
    ans[int(input())] += 1
    
if ans[0] > ans[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")