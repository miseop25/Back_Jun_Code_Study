def balance(new_p):
    u = ''
    v = ''
    if len(new_p) == 0 :
        return u,v,new_p
    
    ok_position = 0
    index_cnt = 0
    for i in new_p :
        if i == '(' :
            ok_position +=1
        else :
            ok_position -=1
        if ok_position  == 0 :
            u = new_p[ :index_cnt+1]
            v = new_p[index_cnt+1: ]
            new_p = new_p[index_cnt+1: ]
            print('u :' , u,'v :', v)
            break
        else : 
            u += i 
        index_cnt +=1
    return u,v, new_p    




def solution(p):
    answer = ''
    new_p = p
    u = ''
    v = ''
    buf = ''
    buf2 = ''
    ok_position = 0 
    u_check = 0
    while True :
        u,v,new_p = balance(new_p)

        for i in u :
            if i == '(' :
                ok_position +=1
            else :
                ok_position -=1
            if ok_position <0 :
                u_check = -1
                break
            elif ok_position ==0 :
                u_check = 1


        if u_check == 1 :
            v = solution(v)
            answer =answer+ u + v
        elif u_check == -1 :
            v = solution(v)   
            u = u[1:-1]
            u = u[::-1]
            u = '(' +v+ ')' + u
            answer = answer + u
            print('del u :', u)


        print('answer',answer)
        if len(answer) >= len(p) :
            return answer

    return answer






