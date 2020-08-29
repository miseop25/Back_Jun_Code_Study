import sys
input = sys.stdin.readline

if __name__ == "__main__":
    mySet = set()
    N,M = map(int, input().split(" "))
    for _ in range(N) :
        mySet.add(input().rstrip())
    
    answer = 0
    for _ in range(M) :
        if input().rstrip() in mySet :
            answer += 1
    
    print(answer)

