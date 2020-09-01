from collections import deque

if __name__ == "__main__":
    N, K = map(int, input().split(" ")) 
    array = deque([i for i in range(1, N+1)]) 
    result = []
    cnt = 0
    while array :
        temp = array.popleft()
        cnt += 1
        if cnt == K :
            result.append(str(temp))
            cnt = 0 
        else :
            array.append(temp)
    answer = "<" + ", ".join(result) + ">"
    print(answer)

