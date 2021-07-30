import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    x = deque(list(map(int, input().split(" "))))
    y = deque(list(map(int, input().split(" "))))
    m1 = min(x)
    m2 = min(y)
    while x[0] != m1 or y[0] != m2 :
        if x[0] != m1 :
            buf = x.popleft()
            x.append(buf)
        if y[0] != m2 :
            buf = y.popleft()
            y.append(buf)
            
    answer = 0
    for i in range(N) :
        answer += x[i]*y[i]
    print(answer)
            
