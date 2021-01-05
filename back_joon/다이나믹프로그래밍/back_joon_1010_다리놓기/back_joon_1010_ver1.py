import sys
input = sys.stdin.readline

def get_aCb(a: int, b: int) :
    
    left = a
    right = b
    for i in range(1, b) :
        left *= a-i
        right *= b-i
    return int(left/right)

if __name__ == "__main__":
    N = int(input())
    for _ in range(N) :
        a,b = map(int, input().split(" "))
        print(get_aCb(b,a))
    

