def solution(numbers):
    
    num_dict = []
    for i in range(10) :
        num_dict.append([])
    
    answer = ''

    for i in range(len(numbers)) :
        buf_str = str(numbers[i])
        buf = int(buf_str[0])
        num_dict[buf].append(numbers[i])
    buf_list = []
    for i in range(9 , -1 , -1) :
        if len(num_dict[i]) != 0 :
            num_dict[i].sort()
            for k in num_dict[i] :
                answer += str(k)
        
            
    print(num_dict)
        
    return answer


ta = [3, 30, 34, 5, 9]
a =solution(ta)
print(a)