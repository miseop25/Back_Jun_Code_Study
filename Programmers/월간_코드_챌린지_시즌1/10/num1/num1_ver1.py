def makeTri(n) :
    resutlt = ''
    v, r = divmod(n,3)
    resutlt += str(r)
    n = v 
    while n != 0 :
        v, r = divmod(n,3)
        if v == 0 :
            resutlt += str(r)
            break
        resutlt += str(r)
        n = v
    return resutlt[::-1]

def backToTen(n) :
    result = 0
    for i , v in enumerate(n) :
        result += (3**i)*int(v)
    return result

def solution(n):
    answer = 0
    answer = backToTen(makeTri(n))
    return answer

print(solution(45))