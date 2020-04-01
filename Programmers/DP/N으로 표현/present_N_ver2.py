def solution(N, number):
    first = [int(str(N)+str(N)), N*N, N//N, N+N]
    if N == number :
        return 1
    elif number in first :
        return 2
    
    num_list = [[5], first]
    
    for i in range(3 , 9) :
        buf = []
        if i == 3 :
            for j in num_list[1] :
                buf.append(int(str(j)+str(N)))
                buf.append(j*N)
                buf.append(j//N)
                buf.append(j+N)
                buf.append(j-N)
        elif i == 4 :
            for j in num_list[1] :
                for k in num_list[1] :
                    buf.append(int(str(j)+str(k)))
                    buf.append(j*k)
                    buf.append(j//k)
                    buf.append(j+k)
                    buf.append(j-k)
            for j in num_list[2] :
                buf.append(int(str(j)+str(N)))
                buf.append(j*N)
                buf.append(j//N)
                buf.append(j+N)
                buf.append(j-N)
        elif i == 5 :
            for j in num_list[2] :
                for k in num_list[1] :
                    buf.append(int(str(j)+str(k)))
                    buf.append(j*k)
                    buf.append(j//k)
                    buf.append(j+k)
                    buf.append(j-k)

            for j in num_list[3] :
                buf.append(int(str(j)+str(N)))
                buf.append(j*N)
                buf.append(j//N)
                buf.append(j+N)
                buf.append(j-N)
        elif i == 6 :
            for j in num_list[3] :
                for k in num_list[1] :
                    buf.append(int(str(j)+str(k)))
                    buf.append(j*k)
                    buf.append(j//k)
                    buf.append(j+k)
                    buf.append(j-k)
            for j in num_list[2] :
                for k in num_list[2] :
                    buf.append(int(str(j)+str(k)))
                    buf.append(j*k)
                    buf.append(j//k)
                    buf.append(j+k)
                    buf.append(j-k)
            
            for j in num_list[4] :
                buf.append(int(str(j)+str(N)))
                buf.append(j*N)
                buf.append(j//N)
                buf.append(j+N)
                buf.append(j-N)
        elif i == 7 :
            for j in num_list[4] :
                for k in num_list[1] :
                    buf.append(int(str(j)+str(k)))
                    buf.append(j*k)
                    buf.append(j//k)
                    buf.append(j+k)
                    buf.append(j-k)
            for j in num_list[3] :
                for k in num_list[2] :
                    buf.append(int(str(j)+str(k)))
                    buf.append(j*k)
                    buf.append(j//k)
                    buf.append(j+k)
                    buf.append(j-k)
            for j in num_list[5] :
                buf.append(int(str(j)+str(N)))
                buf.append(j*N)
                buf.append(j//N)
                buf.append(j+N)
                buf.append(j-N)
        elif i == 8 :
            for j in num_list[5] :
                for k in num_list[1] :
                    buf.append(int(str(j)+str(k)))
                    buf.append(j*k)
                    buf.append(j//k)
                    buf.append(j+k)
                    buf.append(j-k)
            for j in num_list[4] :
                for k in num_list[2] :
                    buf.append(int(str(j)+str(k)))
                    buf.append(j*k)
                    buf.append(j//k)
                    buf.append(j+k)
                    buf.append(j-k)
            for j in num_list[3] :
                for k in num_list[3] :
                    buf.append(int(str(j)+str(k)))
                    buf.append(j*k)
                    buf.append(j//k)
                    buf.append(j+k)
                    buf.append(j-k)
            for j in num_list[6] :
                buf.append(int(str(j)+str(N)))
                buf.append(j*N)
                buf.append(j//N)
                buf.append(j+N)
                buf.append(j-N)
        buf = list(set(buf))
        if number in buf :
            return i
        else :
            buf = sorted(buf)
            for a in range(len(buf)) :
                if buf[a] > 0 :
                    buf = buf[a :]
                    break
            num_list.append(buf)
    return -1


print(solution(5,3600))