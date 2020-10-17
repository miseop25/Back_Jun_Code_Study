import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    answer = []
    resultDict = dict()
    score = []
    cnt = 0
    for _ in range(N) :
        temp = list(map(int, input().split(" ")))
        score.append(temp)
    result = sorted(score, key= lambda x: -x[2])
    
    for i in result :
        if i[0] in resultDict :
            if resultDict[i[0]] < 2 :
                answer.append([i[0], i[1]])
                resultDict[i[0]] += 1
                cnt += 1
        else :
            resultDict[i[0]] = 1
            answer.append([i[0], i[1]])
            cnt += 1
        if cnt == 3 :
            break
    
    for i in answer :
        print(i[0], i[1])

