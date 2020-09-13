from collections import deque

if __name__ == "__main__":
    N = int(input())
    que = deque([])
    for i in range(1, N+1) :
        que.append(i)
    
    for _ in range(N-1) :
        que.popleft()
        que.append(que.popleft())
    print(que[0])