def solution(p):
    ok_position = 0
    answer = ''
    error_position = ''
    N = len(p)
    k=8
    index_cnt = 0
    while k>0:
        for i in p :
            if i == '(' :
                ok_position +=1
            else :
                ok_position -=1 
            if ok_position <0 :
                ok_position +=1
                p =  p[index_cnt:] 
                break
            else : 
                answer += i 
            index_cnt +=1
        
        if len(answer) == N :
            return answer
        
        index_cnt = 0
        k -= 1

    error_position += '('
    print('error_position ', error_position)
    error_position = error_position[::-1]
    print('error_position ', error_position)


    error_position = error_position[:-1]

    print('error_position ', error_position)
    print('answer ', answer)
    answer = answer + error_position
            

    return answer

p = "()))((()"
print(solution(p))




