import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    que = deque([])
    for _ in range(N) :
        cmd = list(map(str, input().rstrip().split(" ")))
        if cmd[0] == "push" :
            que.append(cmd[1])
        elif cmd[0] == "pop" :
            print(que.popleft()) if que else print(-1)
        elif cmd[0] == "size" :
            print(len(que))
        elif cmd[0] == "empty" :
            print(0) if que else print(1)
        elif cmd[0] == "front" :
            print(que[0]) if que else print(-1)
        elif cmd[0] == "back" :
            print(que[-1]) if que else print(-1)
    

            


