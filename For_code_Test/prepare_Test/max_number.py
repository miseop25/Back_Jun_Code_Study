import operator


def solution(numbers):
    
    num_dict = dict()
    answer = ''
    buf_list = []

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
            buf_st = str(num_dict[i][0])
            buf_list.append(str(num_dict[i][0]))


    print(buf_list)
        
    print('numlist : ', num_dict )
    return answer