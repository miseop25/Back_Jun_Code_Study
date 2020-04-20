import sys
input = sys.stdin.readline


def soluction(command) :
    if command[0] == "push" :
        stack.append(int(command[1]))
    elif command[0] == "pop" :
        if stack :
            print(stack.pop())
        else :
            print(-1)
    elif command[0] == "size" :
        print(len(stack))
    elif command[0] == "empty" :
        if stack :
            print(0)
        else :
            print(1)
    elif command[0] == "top" :
        if stack :
            print(stack[-1])
        else :
            print(-1)
        

N = int(input())
stack = []
for _ in range(N) :
    cmd = list(map(str, input().rstrip().split(" ")))
    soluction(cmd)

