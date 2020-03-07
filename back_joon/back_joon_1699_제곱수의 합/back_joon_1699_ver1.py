N = int(input())

cnt = 0


def find_squre(num) :
    half = round(num/2)
    while True :
        half_squre = half**2
        print(half_squre)
        if half_squre >= num :
            half -= 1
        else :  
            return half_squre


while True :
    if N == 0 :
        break
    else :
        buf = find_squre(N)
        N = N - buf 
        cnt += 1
    


print(cnt)