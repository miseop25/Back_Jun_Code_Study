import sys
input = sys.stdin.readline

if __name__ == "__main__":
    M,N = map(int, input().split(" "))
    prime = [True for _ in range(N+1)]
    answer = []
    for i in range(2, N+1) :
        if prime[i] :
            j = i*2
            if i >= M :
                answer.append(i)
            while j <= N :
                prime[j] = False
                j += i
    for i in answer :
        print(i)
            

