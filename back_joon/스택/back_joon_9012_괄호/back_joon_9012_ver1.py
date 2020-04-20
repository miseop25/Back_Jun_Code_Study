import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N) :
    stack = []
    answer = True
    s = input().rstrip()
    for i in s :
        if i == "(" :
            stack.append(i)
        elif i == ")" :
            if stack :
                check = stack.pop()
            else : 
                answer = False
                break
    if stack or answer == False:
        print("NO")
    else :
        print("YES")