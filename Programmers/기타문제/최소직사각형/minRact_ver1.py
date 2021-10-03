def solution(sizes):
    answer = 0
    height = 0
    weight = 0
    for x, y in sizes :
        tw = max(x,y)
        th = min(x,y)
        if tw > weight :
            weight = tw
        if th > height :
            height = th
    answer = weight*height
    return answer