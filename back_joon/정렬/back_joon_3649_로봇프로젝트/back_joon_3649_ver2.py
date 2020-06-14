import sys
input = sys.stdin.readline

def soluction() :
    isInput = input().rstrip()
    if isInput == '' :
        return False
    x = int(isInput) * 10000000
    n = int(input())
        

    lego = dict()
    answer = dict()

    for _ in range(n) :
        k = int(input())
        if k not in lego :
            if x - k >= 0 :
                lego[k] = [x - k, 1]
        else :
            lego[k][1] += 1
    
    for k in lego.keys() :
        if lego[k][0] in lego :
            if k <= lego[k][0] :
                l1 = k
                l2 = lego[k][0]
            else :
                l1 = lego[k][0]
                l2 = k
            if int(x/2) == k :
                if lego[k][1] < 2 :
                    continue
            answer[l1] = [l2 , abs(l1- l2)]
    
    if len(answer) == 0 :
        print("danger")
    else :
        result = sorted(answer.items(), key= lambda x : -x[1][1])
        print("yes", result[0][0], result[0][1][0])
    return True

if __name__ == "__main__":
    isRun = True
    while isRun :
        isRun = soluction()
    