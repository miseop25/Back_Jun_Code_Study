import sys
input = sys.stdin.readline

if __name__ == "__main__":
    x = int(input()) * 10000000
    n = int(input())

    lego = dict()

    for _ in range(n) :
        k = int(input())
        if k not in lego :
            if x - k >= 0 :
                lego[k] = x - k
        
    
    answer = dict()
    for k in lego.keys() :
        if lego[k] in lego :
            if k <= lego[k] :
                l1 = k
                l2 = lego[k]
            else :
                l1 = lego[k]
                l2 = k
            
            
            answer[l1] = [l2 , abs(l1- l2)]
    
    if len(answer) == 0 :
        print("danger")
    else :
        result = sorted(answer.items(), key= lambda x : -x[1][1])
        print("yes", result[0][0], result[0][1][0])

    