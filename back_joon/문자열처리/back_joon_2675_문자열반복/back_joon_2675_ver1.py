import sys
input = sys.stdin.readline

def soluction(word, r) :
    result = ''
    for i in word :
        result += i*r
    return result

if __name__ == "__main__":
    T = int(input())
    for _ in range(T) :
        r, word = map(str, input().rstrip().split(" "))
        print(soluction(word, int(r)))
    