import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    N, M  = map(int, input().split(" "))
    extract = list(map(int, input().split(" ")))
    que = deque([i for i in range(1, N + 1)])
    answer = 0 
    for i in extract :
        f = que.index(i)
        if f < len(que)-f :
            while que[0] != i :
                temp = que.popleft()
                que.append(temp)
                answer += 1
        else :
            while que[0] != i :
                temp = que.pop()
                que.appendleft(temp)
                answer += 1
        que.popleft()
    
    print(answer)
