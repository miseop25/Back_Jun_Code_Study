for _ in range(3) :
    num_list = list(map(int, input().split(' ')))
    answer_list = ['E', 'C','B','A','D']
    ans = sum(num_list)
    print(answer_list[ans])