import sys
import copy
input = sys.stdin.readline


def soluction(sk, width) :
    array = copy.deepcopy(sk)
    answer = 0 
    for i in range(width -1 ) :
        if (array[0][i] + array[1][i+1]) >= (array[0][i+1] + array[1][i])  :
            array[0][i+1] = 0
            array[1][i] = 0
        else :
            array[0][i] = 0
            array[1][i+1] = 0
    for ans in array :
        answer += sum(ans)
    return answer

    
def soluction2(sk, width) :
    answer = 0 
    array = copy.deepcopy(sk)
    for i in range(width-1, 0, -1) :
        if (array[0][i] + array[1][i-1]) >= (array[0][i-1] + array[1][i])  :
            array[0][i-1] = 0
            array[1][i] = 0
        else :
            array[0][i] = 0
            array[1][i-1] = 0
    for ans in array :
        answer += sum(ans)
    return answer



T = int(input())
for _ in range(T) :
    sticker = []
    ans_list = []
    n = int(input())
    for i in range(2) :
        buf = list(map(int, input().split(" ")))
        sticker.append(buf)
    ans_list.append(soluction(sticker, n))
    ans_list.append(soluction2(sticker, n))
    
    print(max(ans_list))
    