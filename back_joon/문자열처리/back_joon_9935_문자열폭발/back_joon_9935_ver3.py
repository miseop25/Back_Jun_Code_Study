import sys
input = sys.stdin.readline

def soluction():
    word = input().rstrip()
    b = input().rstrip()
    if len(word) < len(b) :
        return word
    stack = []

    for  w in word :
        if w == b[-1] :
            if len(stack) >= len(b)-1 :
                flag = True
                for j in range(len(b)-1) :
                    if stack[-j -1] != b[-j -2] :
                        flag = False
                        stack.append(w)
                        break
                if flag :
                    for _ in range(len(b)-1) :
                        stack.pop()
            else :
                stack.append(w)
        else :
            stack.append(w)
    if stack :    
        return "".join(stack)
    else :
        return "FRULA"
        

if __name__ == "__main__":
    print(soluction())
    