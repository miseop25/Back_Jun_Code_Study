N = input()

answer = 0
num_len = len(N)
check = 9

if num_len > 1 :
    for i in range(1 ,num_len) :
        answer += (i * check) 
        check *= 10
    num = int(N) - 10**(num_len-1) +1
    answer += (num_len * num)
else :
    answer = int(N)

print(answer)


