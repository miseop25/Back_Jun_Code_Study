E, S, M = map(int, input().split(' '))

year = 1 

E_f, S_f, M_s = 1,1,1

while True :
    if E_f == E and S_f == S and M_s == M :
        print(year)
        break
    else :
        year +=1
        E_f += 1
        S_f += 1
        M_s += 1

    if E_f == 16 :
        E_f = 1
    if S_f == 29 :
        S_f = 1
    if M_s == 20 :
        M_s = 1
        
