from collections import deque

class Track :
    def __init__(self, board) :
        self.board = board
        self.N = len(board)
        self.check = [[0 for _ in range(self.N) ] for _ in range(self.N) ]

        self.di = [-1, 0, 1, 0]
        self.dj = [0, 1, 0, -1]

    def BFS(self) :
        que = deque()
        que.append((0,0,0,0))
        # i,j,방향, 가격

        while que :
            i,j,k, v = que.popleft()
            for p in range(4) :
                ni = i + self.di[p]
                nj = j + self.dj[p]
                
                if ni < 0 or nj < 0 or ni >= self.N or nj >= self.N  or (ni == 0 and nj == 0 ):
                    continue
                if self.board[ni][nj] == 1 :
                    continue

                if i == 0 and j == 0 :
                    price = 100
                elif k == p :
                    price = v + 100
                else :
                    price = v + 600

                if self.check[ni][nj] == 0 :
                    self.check[ni][nj] = price
                    que.append((ni,nj,p, price))
                elif price <= self.check[ni][nj] :
                    que.append((ni, nj, p, price))
                    self.check[ni][nj] = price
        
    def getAnswer(self) :
        self.BFS()
        return self.check[-1][-1]




def solution(board):
    answer = 0
    t = Track(board)
    answer = t.getAnswer()
    return answer

print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))