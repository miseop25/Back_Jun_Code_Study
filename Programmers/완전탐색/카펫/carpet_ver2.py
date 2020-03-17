def solution(brown, red):
    answer = []
    for i in range(1,red+1) :
        val , temp = divmod(red,i)
        if temp == 0 :
            answer.append([val,i])

    for i in answer :
        total = (i[0]+2)*(i[1]+2)
        if (total - red) == brown :
            return [i[0]+2 , i[1]+2]
    print(answer)

print(solution(8,1))
