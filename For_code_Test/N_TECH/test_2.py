def solution(n):
    answer = 0
    num_list = [1,2,3,4,5,6,7,8,9]
    n_str = str(n)
    for i in n_str :
        n_int = int(i)
        if n_int in num_list :
            if n%n_int == 0 :
                answer +=1
                num_list.remove(n_int)


    return answer