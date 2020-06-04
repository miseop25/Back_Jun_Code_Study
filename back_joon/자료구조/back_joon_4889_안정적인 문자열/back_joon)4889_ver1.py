import sys
input = sys.stdin.readline

def soluction(s) :
    left_stack = []
    cnt = 0
    for i in s :
        if i == "{" :
            left_stack.append(i)
        else :
            if left_stack :
                left_stack.pop()
            else :
                cnt += 1
                left_stack.append("{")
        if i == "-" :
            return -1
    
    if left_stack :
        cnt += len(left_stack)//2
    return cnt


if __name__ == "__main__":
    num = 1
    while True :
        string = input().rstrip()
        answer = soluction(string)
        if answer != -1 :
            result = str(num) + ". " + str(answer)
            print(result)
            num += 1
        else :
            break

    
