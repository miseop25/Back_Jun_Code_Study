import sys
input = sys.stdin.readline

def soluction():
    word = input().rstrip()
    b = input().rstrip()
    
    while True :
        temp = word.split(b)
        answer = ''.join(temp)
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
    