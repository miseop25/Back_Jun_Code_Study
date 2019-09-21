def solution(words, queries):
    where_que = []
    answer = []

    for i in queries :
        que_index = 0
        count = 0
        str_to_list = list(i)
        que_index = str_to_list.index('?')
        if que_index == 0:
            while True:
                que_index+=1
                if str_to_list[que_index] != '?':
                    break
            where_que.append(que_index)
            where_que.append(len(str_to_list)-1)


        else :
            where_que.append(0)
            where_que.append(que_index-1)

        correct_len = where_que[1]-where_que[0] +1

        for k in words :
            mid_cnt = 0 
            if len(k) == len(i) :
                word_to_list = list(k)
                for z in range(where_que[0],where_que[1]+1) :
                    if word_to_list[z] == str_to_list[z]:
                        mid_cnt+=1
                if mid_cnt == correct_len :
                    count+=1

        answer.append(count)
        
        where_que.clear()
        print(str_to_list)
    return answer