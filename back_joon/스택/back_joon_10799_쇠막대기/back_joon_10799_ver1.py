import sys
input = sys.stdin.readline

if __name__ == "__main__":
    bracket = input().rstrip()
    stack = []
    answer = 0
    for i, v in enumerate(bracket) :
        if v == "(" :
            if bracket[i+1] == "(" :
                answer += 1
            stack.append(i)
        elif v == ")" :
            index = stack.pop()
            if i-1 == index :
                answer += len(stack)
    print(answer)
