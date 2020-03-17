def solution(brown, red):
    answer = []
    check = 1

    for i in range(3, 100000) :
        for j in range(i , 100000):
            buf = (i-2)*(j-2)
            total = i*j - buf
            if buf == red and total == brown:
                answer.append([i,j])
                return answer[0]



    return answer