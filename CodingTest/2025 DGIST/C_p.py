#https://www.acmicpc.net/contest/problem/1615/3

input = open(0).readline

student, chapter = map(int, input().split())

study_chap = set()

for _ in range(student):
    s = tuple(map(int,input().split()))
    study_chap.add(s[1:])

if not len(study_chap) == student:
    print(-1)
else:
    answer = [str(pow(2, i)) for i in range(chapter)]
    print(" ".join(answer))
