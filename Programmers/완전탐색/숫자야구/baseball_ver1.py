from itertools import permutations


def solution(baseball):
    

    ball_list = list(permutations([1,2,3,4,5,6,7,8,9], 3))
    answer = []
    cnt = 0

    for k in ball_list :
        buf = k[0]*100 + k[1]*10 + k[2]
        answer.append(buf)
    for i in baseball :
        num = []
        num.append(int(i[0]/100))
        num.append(int(i[0]%100/10))
        num.append(int(i[0]%100%10))
        for ball in ball_list :
            st_cnt = 0
            ba_cnt = 0
            for j in range(3) :
                if ball[j] == num[j] :
                    st_cnt +=1
                elif ball[j] in num :
                    ba_cnt +=1

            if st_cnt == int(i[1]) and ba_cnt == int(i[2]) :
                pass
            else :
                answer[cnt] = 0
        answer=list(set(answer))
        cnt +=1 

    if 0 in answer :
        answer.remove(0)
    
    print((set(ball_list)- set(answer)))

    return len(answer)