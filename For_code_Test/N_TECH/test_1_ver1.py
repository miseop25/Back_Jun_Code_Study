def solution(a, b, budget):
    answer = 0
    n = 1

    while True :
        if n == 0 :
            buf = budget
        else :
            buf -= b 
            n= 1


        if buf <0 :
            break
        elif buf == 0:
            answer +=1
            break

        mod =  buf%a
        if mod == 0 :
            answer +=1


    return answer