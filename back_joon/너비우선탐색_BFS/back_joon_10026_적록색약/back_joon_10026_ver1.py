import sys
input = sys.stdin.readline

def checkImage(x, y,color) :
    dx = [-1, 1, 0,0]
    dy = [0, 0, -1, 1]
    cnt = 0

    BFS[x][y] = 1
    for i in range(4): 
        tx = x + dx[i]
        ty = y + dy[i]
        if tx >= 0 and tx < N and ty >= 0 and ty < N :
            if board[tx][ty] == color and BFS[tx][ty] == 0 :
                BFS[tx][ty] = 1
                checkImage(tx, ty, color)
                cnt = 1
    return cnt
    


if __name__ == "__main__":
    N = int(input())
    rgPerson = {"rg" : [], "b" : []}
    normalPerson = {"R": [], "G" : [], "B" : []}
    BFS = [[0 for i in range(N)] for j in range(N)]
    board = []

    for i in range(N) :
        temp = input().rstrip()
        for j in range(N) :
            if temp[j] == "R" :
                rgPerson["rg"].append([i,j])
                normalPerson["R"].append([i,j])
            elif temp[j] == "G" :
                rgPerson["rg"].append([i,j])
                normalPerson["G"].append([i,j])
            else :
                rgPerson["b"].append([i,j])
                normalPerson["B"].append([i,j])
        board.append(temp)
    
    print(board)

    norAnswer = 0
    rgAnswer = 0

    for n in normalPerson.keys() :
        for x, y in normalPerson[n] :
            norAnswer += checkImage(x,y, n)
    print(norAnswer)
            
