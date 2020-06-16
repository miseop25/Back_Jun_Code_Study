import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    answer = 0
    for _ in range(N) :
        stack = []
        check = True
        temp = input().rstrip()
        length = len(temp)
        if length%2 != 0 :
            continue
        for i in temp[: length//2 ] :
            if stack :
                if stack[-1] == i :
                    stack.pop()
                else :
                    stack.append(i)
            else :
                stack.append(i)

        for i in temp[length//2 : ] :
            if stack :
                if stack[-1] == i :
                    stack.pop()
                else :
                    check = False
                    break
            else :
                stack.append(i)
        if len(stack) == 0 and check :
            answer += 1
        
    print(answer)