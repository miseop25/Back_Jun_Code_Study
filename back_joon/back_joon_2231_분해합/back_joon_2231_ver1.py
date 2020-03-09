def sumEachNum(num) :
    answer = int(num)
    for i in range(len(num)) :
        answer += int(num[i])
    return answer


N = input()
sum_value = int(N)
min_value = sum_value - len(N)*9
if min_value <0 :
    min_value = 0
min_str = str(min_value)

while True :
    check = sumEachNum(min_str)
    if sum_value == check :
        break
    else :
        min_str = str(int(min_str) + 1)


    if sum_value == int(min_str) :
        min_str = 0
        break

print(min_str)