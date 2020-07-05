num = "0123456789ABCDEF"

def changeN(n, base):
    val, rem = divmod(n, base)
    c = num[rem]
    return changeN(val, base) + c if val else c

def solution(n, t, m, p):
    answer = ''
    number = ''
    i = 0
    myTurn = p -1
    while len(answer) < t :
        number += changeN(i, n)
        while len(number) > myTurn and len(answer) < t :
            answer += number[myTurn]
            myTurn += m
        i += 1
    return answer

print(solution(16,16,2,1))