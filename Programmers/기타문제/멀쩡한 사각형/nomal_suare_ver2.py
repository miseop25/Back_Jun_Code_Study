import math
def solution(w,h):
    answer = 0

    if w == 1 or h == 1 :
        return 0
    if w == h :
        return w*h - w
    
    if w < h :
        x = w 
        y = h
    else :
        x = h
        y = w 
    val , leave = divmod(y, x)
    if leave != 0 :
        val += 1
    answer = (w*h) - (val * x)
    return answer