import sys
input = sys.stdin.readline

N, s, p = map(int, input().split(" "))
if N == 0 :
    # 랭킹 리스트가 비어있는경우 
    score_list = []
else :
    score_list = list(map(int, input().split(" ")))

answer = [0, 0]
#  answer[0] 은 등수, answer[1] 은 순번이다.
if s in score_list :
    temp = score_list.index(s)
    answer[1] = temp + 1
    cnt = 0
    for i in score_list[temp : ] :
        if i == s :
            cnt += 1 
        else : 
            break
    answer[0] = temp + cnt + 1
else :
    score_list.append(s)
    score_list = sorted(score_list, reverse= True)
    answer[0] = score_list.index(s) + 1
    answer[1] = score_list.index(s) + 1

if answer[0] <= p :
    print(answer[1])
else :
    print(-1)

        