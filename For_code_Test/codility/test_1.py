# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    #alpabet = ['a', 'b', 'c','d','e','f','g','h', 'i', 'j','k','l', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    buf_list = []
    cnt = 1
    for i in A :
        for j in i :
            if j in buf_list :
                cnt = -1
                break


        if cnt == -1 :
            A.remove(i)
            cnt = 1 


    print(buf_list)
    print(A)

    pass

print(solution(['abc', 'yyy', 'def', 'csv'] ))