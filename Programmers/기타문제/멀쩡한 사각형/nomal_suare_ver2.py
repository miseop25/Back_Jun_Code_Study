import math
def solution(w,h):
    answer = 0

    if w == 1 or h == 1 :
        return 0
    if w == h :
        return w*h - w
    
    gcd_num = math.gcd(w,h)
    if gcd_num == 1:
        answer = w*h - (w + h - 1)
    else :
        answer = w * h - (w + h - gcd_num)
    return answer