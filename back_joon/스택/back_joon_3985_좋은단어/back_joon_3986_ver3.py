import sys
input = sys.stdin.readline

def checkWord(word) :
    stack = []
    for i in word :
        if stack :
            if stack[-1] == i :
                stack.pop()
            else :
                stack.append(i)
        else :
            stack.append(i)
    if stack :
        return False
    else :
        return True


if __name__ == "__main__":
    N = int(input())
    answer = 0
    for _ in range(N) :
        word = input().rstrip()
        if checkWord(word) :
            answer += 1
    print(answer)