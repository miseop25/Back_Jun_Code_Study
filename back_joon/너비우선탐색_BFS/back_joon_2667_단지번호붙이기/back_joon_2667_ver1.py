import sys
input = sys.stdin.readline

def checkVillige(x, y) :
    dx = [-1, 1, 0,0]
    dy = [0, 0, -1, 1]
    cnt = 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx >= 0 and tx < N and ty >= 0 and ty < N :
            if BFS[tx][ty] == 0 and villige[tx][ty] == "1" :
                BFS[tx][ty] = 1
                cnt += checkVillige(tx, ty)
    return cnt


if __name__ == "__main__":
    N = int(input())
    BFS = [[0 for i in range(N)] for j in range(N)]
    house = []
    villige = []
    for i in range(N) :
        temp = input().rstrip()
        for j in range(N) :
            if temp[j] == '1' :
                house.append([i,j])
        villige.append(temp)
    answer = 0
    ans_list = []
    for x, y in house :
        if BFS[x][y] == 0 :
            answer += checkVillige(x, y) - 1
            if answer == 0 :
                answer = 1
            ans_list.append(answer)
            answer = 0
    ans_list = sorted(ans_list)
    print(len(ans_list))
    for i in ans_list :
        print(i)
    


    