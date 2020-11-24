import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    num = list(map(int, input().rstrip().split(" ")  ))
    stack_A = []
    stack_B = []
    data = 1
    
    for i in num :
        for _ in range(i) :
            stack_B.append(stack_A.pop())
        stack_A.append(str(data))
        for _ in range(i) :
            stack_A.append(stack_B.pop())
        data += 1
    print(" ".join(stack_A))
