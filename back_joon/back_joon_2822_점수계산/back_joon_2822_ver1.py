score_list = []
total_Score = 0
answer_list = []

for i in range(8) :
    score = int(input())
    score_list.append([])
    score_list[i].append(score)
    score_list[i].append(i+1)


score_list = sorted(score_list, key=lambda x: x[0], reverse= True)
for i in range(5):
    total_Score += score_list[i][0]
    answer_list.append(score_list[i][1])

answer_list = sorted(answer_list)
ans = str(answer_list[0])

for i in answer_list[1:] :
    ans = ans +  " " + str(i)


print(total_Score)
print(ans)
