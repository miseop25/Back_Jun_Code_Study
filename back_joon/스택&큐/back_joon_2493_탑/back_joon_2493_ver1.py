import sys
input = sys.stdin.readline

def checkRecive(index, tall) :
    for t in range(index-1, -1, -1) :
        if top[t] > tall :
            answer[index] = str(t + 1)
            break


if __name__ == "__main__":
    N = int(input())
    top = list(map(int, input().split(" ")))
    answer = ['0' for i in range(N) ]
    for i in range(N-1, -1, -1) :
        checkRecive(i, top[i])

    print(" ".join(answer))

