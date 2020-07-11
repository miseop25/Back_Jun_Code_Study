def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, key= lambda x: -x)
    for i in range(len(A)) :
        answer += A[i]*B[i]
    return answer