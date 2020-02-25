import sys

for _ in range(3) :
    num_list = list(map(int, input().split(' ')))
    answer_list = ['D', 'C','B','A','E']
    ans = sum(num_list)
    print(answer_list[ans])