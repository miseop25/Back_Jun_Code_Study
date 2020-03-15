def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=len)
    check = 1

    for i in phone_book :
        temp = len(i)
        for j in phone_book :
            if j[:temp] == i :
                if i != j :
                    answer = False
                    check = -1
                    break
        if check == -1 :
            break
    return answer


print(solution(['119', '97674223', '1195524421']))