import sys
input=sys.stdin.readline


def soluction(cnt,val, buf) : 
    answer = []
    if cnt == 1:
        answer.append([cnt, val])
        cnt +=1
        answer.append([cnt, val + buf])
    elif cnt == 0 :
        cnt += 1
        answer.append([cnt, val + buf])
    else :
        cnt = 0 
        answer.append([cnt, val])
    
    return answer

ans_list = []
for i in range(int(input())):
    buf = int(input())
    buf_list = []
    if i == 0 :
        ans_list.append([0])
        ans_list[0].append(0)

        ans_list.append([1])
        ans_list[1].append(buf)


    else :
        for k in ans_list :
            buf_list.extend(soluction(k[0], k[1], buf))

        ans_list = buf_list

ans_list.sort(key=lambda x : x[1], reverse= True)
print(sys.getsizeof(ans_list))
print(ans_list[0][1])