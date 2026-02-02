# 백준 3460 : 이진수

# https://www.acmicpc.net/problem/3460

input = open("input.txt").readline

cases = int(input())

def find_one_poses(n):
    poses = []

    pos = 0
    
    while n:
        if n%2:
            poses.append(pos)
        
        n //= 2
        pos += 1
    
    print(" ".join(map(str, poses)))

for _ in range(cases):
    find_one_poses(int(input()))
