# 10102 : 개표
# https://www.acmicpc.net/problem/10102

length = int(input())

vote = input()

A_vote_cnt = vote.count("A")
B_vote_cnt = vote.count("B")

if A_vote_cnt > B_vote_cnt:
    print("A")
elif A_vote_cnt < B_vote_cnt:
    print("B")
else:
    print("Tie")