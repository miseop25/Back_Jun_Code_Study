import sys
input = sys.stdin.readline

    

def soluction() :
    N , M = map(int, input().split(" "))
    for _ in range(M) :
        _,_ = map(int, input().split(" "))    
    return N-1
if __name__ == "__main__":
    T = int(input())
    for _ in range(T) :
        print(soluction())

