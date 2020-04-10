import sys
input = sys.stdin.readline
N = int(input())


def soluction(N) :
    answer = []
    result = []
    if N != 1 :
        temp = int(input())
        answer.append([temp, 1])
        answer.append([0, 0])
    else :
        return int(input())
    for _ in range(1, N-1) :
        temp = int(input())
        case1 = []
        case2 = []
        case3 = []
        buf = []
        for i in answer :
            if i[1] == 1 :
                case3.append([i[0]+ temp, 2])
                case1.append([i[0], 0])
            elif i[1] == 0 :
                case2.append([i[0]+ temp, 1])
            elif i[1] == 2 :
                case1.append([i[0], 0])
        
        case1 = sorted(case1, key= lambda x: x[0], reverse=True)
        case2 = sorted(case2, key= lambda x: x[0], reverse=True)
        case3 = sorted(case3, key= lambda x: x[0], reverse=True)
        if case1 :
            buf.append(case1[0])
        if case2 :
            buf.append(case2[0])
        if case3 : 
            buf.append(case3[0])
        answer = buf

    last = int(input())
    for i in answer :
        if i[1] != 2 :
            result.append(i[0] + last )
    return max(result)

print(soluction(N))

