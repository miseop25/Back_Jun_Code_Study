import operator


def solution(numbers):
    
    num_dict = dict()
    answer = ''
    buf_list = []
    buf_int = -1
    cnt = -1

    for i in numbers :
        buf = str(i)
        num_dict[i] = int(buf[0])
    num_dict = sorted(num_dict.items(), key = operator.itemgetter(1), reverse= True)
    print(num_dict)

    for i in range(len(num_dict)) :
        buf = len(str(num_dict[i][0])) #자릿수 확인하는 버퍼 
        if buf == 1 :
            answer += str(num_dict[i][0])
        else :
            if buf_int == int(num_dict[i][1]) :
                buf_list.sort()
                for k in buf_list :
                    answer += str(k)
                cnt = 1
            else :
                buf_int = int(num_dict[i][1])
                buf_list.append((num_dict[i][0]))

    if cnt == -1 :
        buf_list.sort()
        for k in buf_list :
            answer += str(k)
    

        
    print('numlist : ', num_dict )
    return answer


ta = [3, 30, 34, 5, 9]
a =solution(ta)
print(a)