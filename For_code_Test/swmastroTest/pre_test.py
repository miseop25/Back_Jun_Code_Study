import sys
input = sys.stdin.readline

N, K = map(int, input().split(" "))
num_list = list(map(int, input().split(" ")))

one_index = num_list.index(1)

if one_index > K :
    after_one = (N-one_index-1)//(K-1)
    before_one = (one_index - 1)//(K-1)
    ans = after_one + before_one
else :
    ans = N//(K-1)



print(ans)
