# 백준 6376 : e 계산

# https://www.acmicpc.net/problem/6376

input = open("input.txt").readline

i_fac = 1

e = 0

print("n e")
print("- -----------")

for n in range(10):
    print(n, end=" ")
    
    i_fac *= (n if n else 1)
    e += 1/i_fac

    if n == 8:
        print(str(round(e, 9))+"0")
    else:
        print(int(e) if not e%1 else round(e, 9))

