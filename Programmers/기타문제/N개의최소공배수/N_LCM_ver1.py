import math
def solution(arr):
    answer = arr[0]
    if len(arr) == 1:
        return answer
    for i in arr[1 :] :
        answer = (answer* i) // math.gcd(answer, i)
    
    return answer