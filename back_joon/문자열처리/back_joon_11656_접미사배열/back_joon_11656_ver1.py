S = input().rstrip()

answer = []
for i in range(len(S)) :
    answer.append(S[i:])
answer.sort()
for j in answer :
    print(j)

