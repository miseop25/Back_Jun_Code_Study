import sys
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__":
    N = int(input())
    que = deque([])
    cnt = 0
    for _ in range(N) :
        cmd = list(input().rstrip().split(" "))
        if cmd[0] == "push_back" :
            que.append(cmd[1])
            cnt += 1
        elif cmd[0] == "push_front" :
            que.appendleft(cmd[1])
            cnt += 1
        elif cmd[0] == "pop_front" :
            if que :
                print(que.popleft())
                cnt -= 1
            else :
                print(-1)
        elif cmd[0] == "pop_back" :
            if que :
                print(que.pop())
                cnt -= 1
            else :
                print(-1)
        elif cmd[0] == "size" :
            print(cnt)
        elif cmd[0] == "empty" :
            if que :
                print(0)
            else :
                print(1)
        elif cmd[0] == "front" :
            if que :
                print(que[0])
            else :
                print(-1)
        elif cmd[0] == "back" :
            if que :
                print(que[-1])
            else :
                print(-1)

