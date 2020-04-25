import sys
input = sys.stdin.readline


N = int(input())
card = dict()
for _ in range(N) :
    num = int(input())
    if num in card :
        card[num] += 1
    else :
        card[num] = 1
answer = sorted(card.items(), key= lambda x: (-x[1], x[0]))
print(answer)
print(answer[0][0])