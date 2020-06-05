import copy
import sys
input = sys.stdin.readline

def checkMap(ch) :
    if ch == "J" :
        return [1,0,0]
    elif ch == "O" :
        return [0,1,0]
    else :
        return [0,0,1]

    


if __name__ == "__main__":
    M, N = map(int, input().split(" "))
    K = int(input())
    plantMap = []
    
    for i in range(M) :
        line = input().rstrip()
        buf = []
        real = []
        temp = [0,0,0]
        for c in range(N) :
            plus = checkMap(line[c])
            for p in range(3) :
                temp[p] += plus[p]
            buf.append(copy.deepcopy(temp))
            if i != 0 :
                b_Temp = copy.deepcopy(temp)
                for p in range(3) :
                    b_Temp[p] += plantMap[i-1][c][p]
                real.append(copy.deepcopy(b_Temp))    

        if i == 0 :
            plantMap.append(copy.deepcopy(buf))
        else :
            plantMap.append(copy.deepcopy(real))
    
    for i in range(K) :
        a, b, c, d = map(int, input().split(" "))
        if a != 1 and b != 1:
            J = plantMap[c-1][d-1][0] - plantMap[c-1][b-2][0] - (plantMap[a-2][d-1][0] - plantMap[a-2][b-2][0])
            O = plantMap[c-1][d-1][1] - plantMap[c-1][b-2][1] - (plantMap[a-2][d-1][1] - plantMap[a-2][b-2][1])
            I = plantMap[c-1][d-1][2] - plantMap[c-1][b-2][2] - (plantMap[a-2][d-1][2] - plantMap[a-2][b-2][2])
        elif a == 1 and b != 1 :
            J = plantMap[c-1][d-1][0] - plantMap[c-1][b-2][0]
            O = plantMap[c-1][d-1][1] - plantMap[c-1][b-2][1] 
            I = plantMap[c-1][d-1][2] - plantMap[c-1][b-2][2] 
        elif b == 1 and a != 1 :
            J = plantMap[c-1][d-1][0]  - plantMap[a-2][d-1][0]
            O = plantMap[c-1][d-1][1]  - plantMap[a-2][d-1][1]
            I = plantMap[c-1][d-1][2]  - plantMap[a-2][d-1][2]
        else :
            J = plantMap[c-1][d-1][0]
            O = plantMap[c-1][d-1][1] 
            I = plantMap[c-1][d-1][2]



        print(J, O ,I)