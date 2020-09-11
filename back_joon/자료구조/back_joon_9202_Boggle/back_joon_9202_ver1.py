import sys
input = sys.stdin.readline

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = dict()
        self.isEnd = False

class Boggle : 
    def __init__(self, N) :
        self.wordDict = dict()
        self.N = N
        self.dx = [-1, -1, -1, 0, 0, 1, 1, 1] 
        self.dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        self.result = set()

    # Trie 자료구조에 단어 삽입하기
    def makeTrie(self, temp) :
        if temp[0] in self.wordDict :
            pre = self.wordDict[temp[0]]
        else :
            self.wordDict[temp[0]] = Node(temp[0])
            pre = self.wordDict[temp[0]]
        if len(temp) == 1 :
            pre.isEnd = True
        for i in range(1, len(temp)):
            if temp[i] not in pre.next :
                pre.next[temp[i]] = Node(temp[i])
            pre = pre.next[temp[i]]
            if i == len(temp)-1 :
                pre.isEnd = True
    
    # Trie 자료구조에 단어 삽입하기
    def wordInput(self) :
        for _ in range(self.N) :
            temp = input().rstrip()
            self.makeTrie(temp)

    # 주어진 보드 입력받기
    def myBoard(self) :
        board = []
        for _ in range(4) :
            board.append(list(input().rstrip()))
        return board
    
    # i, j 인덱스에서 단어 탐색하기
    def findWord(self, board, i,j, bfs, word, st) :
        word += board[i][j]
        if st.isEnd :
            self.result.add(word)
        bfs[i][j] = 1
        for k in range(8) :
            x = i + self.dx[k]
            y = j + self.dy[k]
            if x < 0 or x > 3 or y < 0 or y > 3 :
                continue
            if bfs[x][y] != 0 :
                continue
            if board[x][y] in st.next : 
                self.findWord(board, x,y,bfs,word, st.next[board[x][y]])
                bfs[x][y] = 0


    def printAnswer(self) :
        point = str(self.checkPoint())
        maxWord = self.checkMaxWord()
        cnt = str(len(self.result))
        answer = point + " " + maxWord + " " + cnt
        return answer

    def checkMaxWord(self) :
        temp = sorted(self.result, key= lambda x: (-len(x), x) )
        return temp[0]

    def checkPoint(self) :
        point = 0
        for i in self.result :
            if len(i) < 3 :
                continue
            elif len(i) < 5 :
                point += 1
            elif len(i) == 5 :
                point += 2
            elif len(i) == 6 :
                point += 3
            elif len(i) == 7 :
                point += 5
            elif len(i) == 8 :
                point += 11
        return point
    
    def soluction(self) :
        board = self.myBoard()
        self.result.clear()
        for i in range(4) :
            for j in range(4) :
                bfs = [[0 for _ in range(4)] for _ in range(4)] 
                if board[i][j] in self.wordDict :
                    st = self.wordDict[board[i][j]]
                    self.findWord(board, i,j, bfs, '' , st)
        print(self.printAnswer())

if __name__ == "__main__":
    N = int(input())
    test = Boggle(N)
    test.wordInput()
    input().rstrip()
    K = int(input())
    test.soluction()
    for _ in range(K-1) :
        input()
        test.soluction()
        