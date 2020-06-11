import sys
input = sys.stdin.readline

def checkStack(tall) :
    while stack :
        if stack[-1][0] < tall :
            stack.pop()
        else :
            answer[i] = str(stack[-1][1] + 1)
            break
    stack.append([tall, i])


if __name__ == "__main__":
    N = int(input())
    top = list(map(int, input().split(" ")))
    answer = ['0' for i in range(N) ]
    stack = [ [top[0], 0] ]
    for i in range(1, N) :
        checkStack(top[i])
    print(" ".join(answer))

