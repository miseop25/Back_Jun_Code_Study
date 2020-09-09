def solution(m, n, puddles):
    answer = 0
    myMap = [[0 for _ in range(m+ 1)] for _ in range(n+1) ]
    myMap[1][1] = 1
    for i in range(1, n+1) :
        for j in range(1, m+1) :
            if i == 1 and j == 1 : continue 
            if [j, i] in puddles :
                myMap[i][j] = 0
            else :
                myMap[i][j] = myMap[i-1][j] + myMap[i][j-1]
    answer = myMap[-1][-1]%1000000007
    return answer

print(solution(4,3, [[2,2]]))