import sys
input = sys.stdin.readline

def checkImage(x, y,color) :
    dx = [-1, 1, 0,0]
    dy = [0, 0, -1, 1]

    BFS[x][y] = 1 
    for i in range(4): 
        tx = x + dx[i]
        ty = y + dy[i]
        if tx >= 0 and tx < N and ty >= 0 and ty < N :
            if board[tx][ty] == color and BFS[tx][ty] == 0 :
                BFS[tx][ty] = 1
                checkImage(tx, ty, color)
    return 1

def checkRGImage(x, y, color) :
    dx = [-1, 1, 0,0]
    dy = [0, 0, -1, 1]

    RG_BFS[x][y] = 1
    for i in range(4): 
        tx = x + dx[i]
        ty = y + dy[i]
        if tx >= 0 and tx < N and ty >= 0 and ty < N :
            if color == "RG" :
                if (board[tx][ty] == "R" or board[tx][ty] == "G") and RG_BFS[tx][ty] == 0 :
                    RG_BFS[tx][ty] = 1
                    checkRGImage(tx, ty, color)
            else :
                if board[tx][ty] == color and RG_BFS[tx][ty] == 0 :
                    RG_BFS[tx][ty] = 1
                    checkRGImage(tx, ty, color)
    return 1
    



if __name__ == "__main__":
    N = int(input())
    rgPerson = {"RG" : [], "B" : []}
    normalPerson = {"R": [], "G" : [], "B" : []}
    BFS = [[0 for i in range(N)] for j in range(N)]
    RG_BFS = [[0 for i in range(N)] for j in range(N)]
    board = []

    for i in range(N) :
        temp = input().rstrip()
        for j in range(N) :
            if temp[j] == "R" :
                rgPerson["RG"].append([i,j])
                normalPerson["R"].append([i,j])
            elif temp[j] == "G" :
                rgPerson["RG"].append([i,j])
                normalPerson["G"].append([i,j])
            else :
                rgPerson["B"].append([i,j])
                normalPerson["B"].append([i,j])
        board.append(temp)
    
    norAnswer = 0
    rgAnswer = 0

    for n in normalPerson.keys() :
        for x, y in normalPerson[n] :
            if BFS[x][y] != 1 :
                norAnswer += checkImage(x,y, n)
    
    for rg in rgPerson.keys() :
        for x, y in rgPerson[rg] :
            if RG_BFS[x][y] != 1 :
                rgAnswer += checkRGImage(x, y, rg)
    

    print(norAnswer, rgAnswer)
            
