def solution(n, stations, w):
    if n == 0 : return 0
    answer = 0
    letft = 1
    width = w*2 + 1
    for i in stations :
        right = i - w 
        if right <= 1 or right <letft:
            letft = i + w +1
            continue
        v, r = divmod(right - letft, width)
        if r == 0 :
            answer += v
        else :
            answer += v + 1
        letft = i + w +1
    if letft <= n :
        v, r = divmod(n+1 - letft, width)
        if r == 0 :
            answer += v
        else :
            answer += v + 1
    return answer

print(solution(100, [1], 1))