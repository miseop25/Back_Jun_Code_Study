import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, K  = map(int, input().split(" "))
    num = list(map(int, input().rstrip().split(" ")))
    total = 0
    psum = []
    sDict = dict()
    answer = 0
    for i , val in enumerate(num) :
        total += val
        psum.append(total)
    
    for i in range(N) :
        if psum[i] == K :
            answer += 1
        if psum[i]- K in  sDict : 
            answer += sDict[psum[i]- K]
        
        if psum[i] in sDict :
            sDict[psum[i]] += 1
        else :
            sDict[psum[i]] = 1
    

    print(answer)

