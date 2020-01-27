# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    bin_N = str(bin(N))

    length_list =[]

    length = 0
    for i in bin_N[3 :] :
        buf = int(i)
        if buf == 1 :
            length_list.append(length)
            length = 0
        else :
            length +=1
    if length_list :
        return(max(length_list))
    else :
        return 0

N = int(input())
print(solution(N))