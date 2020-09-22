import sys
input = sys.stdin.readline

def soluction(N, data) :
    answer = [0 for _ in range(N)]
    check = [0 for _ in range(11)]

    for i in range(N) :
        cnt = 0
        for j in range(N) :
            if cnt == data[i] and check[j] == 0 :
                check[j] = 1
                answer[j] = str(i+1)
                break
            elif check[j] == 0 :
                    cnt += 1
        
    return ' '.join(answer)

if __name__ == "__main__":
    N = int(input())
    data = list(map(int, input().split(" ")))
    print(soluction(N, data))