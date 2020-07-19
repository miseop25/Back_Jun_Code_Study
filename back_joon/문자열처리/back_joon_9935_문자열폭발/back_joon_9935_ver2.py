import sys
input = sys.stdin.readline

def soluction():
    word = input().rstrip()
    b = input().rstrip()
    
    while True :
        answer = word.replace(b, "")
        if answer != word :
            word = answer
        else :
            break
        
    if answer != '' :
        return answer
    else :
        return "FRULA"
        

if __name__ == "__main__":
    print(soluction())
    