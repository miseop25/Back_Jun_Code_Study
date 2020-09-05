import sys
import heapq
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    que = []
    for _ in range(N) :
        cmd = int(input())
        if cmd == 0 :
            if que :
                print(heapq.heappop(que)[1])
            else :
                print(0)
        else :
            heapq.heappush(que, (-cmd, cmd))
    
