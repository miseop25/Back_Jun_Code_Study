from collections import deque
def soluction() :
    N, K, M = map(int, input().split(" "))
    num = deque([])

    for i in range(1 , N+1) :
        num.append(i)

    i = 0
    cnt = 0
    while True :
        i += 1
        buf = num.popleft()
        if i == K :
            cnt += 1
            if buf == M :
                return cnt
            i = 0
        else :
            num.append(buf)
    
if __name__ == "__main__":
    print(soluction())
    