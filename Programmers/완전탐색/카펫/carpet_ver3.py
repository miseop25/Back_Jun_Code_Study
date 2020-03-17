import math
def solution(brown, red):
    answer = []
    t = red + brown 
    c = (t-red + 4)//2

    y = (c + pow(((c*c) - (4 * t)), 0.5)) // 2
    x = c-y
    answer.append(math.floor(y))
    answer.append(math.floor(x))
    return answer

print(solution(8,1))
