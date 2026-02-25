input = open(0).readline

nums = list(map(int, input().split()))

check = 0
answer = min(nums) - 1

while check < 3:
    answer += 1
    check = 0
    
    for n in nums:
        if not answer%n:
            check += 1

print(answer)