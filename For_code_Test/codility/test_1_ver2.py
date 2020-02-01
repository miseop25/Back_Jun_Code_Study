# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import itertools


def solution(A):
    buf_list = []
    fi_ans_list = []
    cnt = 1

    for i in A :
        for j in i :
            if j in buf_list :
                cnt = -1
                break
            else :
                buf_list.append(j)


        if cnt == -1 :
            cnt = 1
        else :
            fi_ans_list.append(i)
        buf_list = []
        
    if A :
        pass 
    else :
        return 0

    length = len(fi_ans_list)
    while True :
        ans_list = list(map(''.join, itertools.permutations(fi_ans_list,length)))
        se_ans = []
        len_list = []
        for i in ans_list :
            for j in i :
                if j in buf_list :
                    cnt = -1
                    break
                else :
                    buf_list.append(j)


            if cnt == -1 :
                cnt = 1
            else :
                se_ans.append(i)
            buf_list = []

        if se_ans :
            for i in se_ans :
                len_list.append(len(i))
            len_list.sort(reverse=True)
            return len_list[0]
        else :
            length -= 1


print(solution(['abc', 'yyy', 'def', 'csv'] ))