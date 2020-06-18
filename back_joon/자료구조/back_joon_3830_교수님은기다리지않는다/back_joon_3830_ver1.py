import sys
input = sys.stdin.readline

def soluction() :
    N , M = map(int, input().split(" "))
    if N == 0 and M == 0 :
        return False
    
    
    return True

if __name__ == "__main__":
    isRun = True
    while isRun :
        isRun = soluction()