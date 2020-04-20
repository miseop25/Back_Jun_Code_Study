N = int(input())
answer = []

for i in range(N):
    answer.append(input())

answer = list(set(answer))
answer = sorted(answer, key=lambda x: (len(x),x) )


for i in answer :
    print(i)