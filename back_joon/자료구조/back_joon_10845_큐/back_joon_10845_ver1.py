import sys
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    que = deque([])
    for _ in range(N) :
        cmd = list(input().rstrip().split(" "))
        if cmd[0] == "push" :
            que.append(cmd[1])
        elif cmd[0] == "pop" :
            if que :
                print(que.popleft())
            else :
                print(-1)
        elif cmd[0] == "size" :
            print(len(que))
        elif cmd[0] == "empty" :
            if que :
                print(0)
            else :
                print(1)
        elif cmd[0] == "front" :
            if que :
                print(que[0])
            else:
                print(-1)
        elif cmd[0] == "back" :
            if que :
                print(que[-1])
            else :
                print(-1)
                