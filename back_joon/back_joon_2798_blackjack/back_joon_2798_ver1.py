def black_jack(N,M,card_num) :
    answer_list = []
    for i in range(N-2) :
        for j in range(i+1, N-1) :
            for k in range(j+1 , N) :
                ans_buf = card_num[i] + card_num[j] + card_num[k]
                if ans_buf == M :
                    return ans_buf
                elif ans_buf < M :
                    answer_list.append(ans_buf)
    answer_list.sort()
    return answer_list.pop()

N,M =  map(int, input().split(' '))
card_num = input().strip().split(' ')
card_num = list(map(int , card_num))
print(black_jack(N,M,card_num))        
        