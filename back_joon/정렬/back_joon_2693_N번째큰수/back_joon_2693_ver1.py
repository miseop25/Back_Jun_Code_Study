import sys
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T) :
        temp = list(map(int, input().split(" ")))
        temp = sorted(temp)
        print(temp[7])
