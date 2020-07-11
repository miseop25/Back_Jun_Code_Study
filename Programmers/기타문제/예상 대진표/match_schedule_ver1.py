def solution(n,a,b):
    answer = 0
    if abs(b-a) == 1 :
        return 1 
    check = int(abs(b-a)**0.5)
    answer = check + 1



    return answer