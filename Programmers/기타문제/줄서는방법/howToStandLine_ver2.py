import math
def solution(n, k):
    answer = []
    num = [i for i in range(1, n+1)]
    while num :
        total = math.factorial(len(num))
        mid = total/len(num)
        v, r = divmod(k,mid)
        if r == 0 : v -= 1
        answer.append(num.pop(int(v)))
        k = k - v*mid 

    return answer


print(solution(3,5))