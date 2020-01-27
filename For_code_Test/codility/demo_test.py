# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    answer = 1
    cnt = 1
    A = sorted(A)
    for i in A :
        if i >0 :
            if i > answer :
                if cnt == -1 :
                    answer +=1
                    cnt = 1
                    if i > answer :
                        return answer
                    else :
                        answer +=1
            elif i == answer :
                cnt = -1
                continue
            else :
                answer +=1

    if cnt != -1 :
        return answer
    else : 
        return answer +1



print(solution([1,2,3]))