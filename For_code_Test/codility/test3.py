# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    buf = A[0]
    ans_list = []
    cnt = 0
    for i in A[1 :] :
        if i == buf :
            cnt +=1
            if buf == 1 :
                buf = 0
            else :
                buf = 1
        else :
            buf = i

    ans_list.append(cnt)

    cnt = 1 
    if A[0] == 1 :
        buf = 0
    else :
        buf = 1

    for i in A[1 :] :
        if i == buf :
            cnt +=1
            if buf == 1 :
                buf = 0
            else :
                buf = 1
        else :
            buf = i
    ans_list.append(cnt)

    ans_list.sort()
    return ans_list[0]


print(solution([1,1,0,1,1]))