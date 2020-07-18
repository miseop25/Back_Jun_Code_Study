import sys
input = sys.stdin.readline

def soluction():
    answer = []
    N = int(input())
    card = list(map(int, input().split(" ")))
    cDict = dict()
    for i in card :
        cDict[i] = True
    M = int(input())
    my = list(map(int, input().split(" ")))
    for i in my :
        if i in cDict :
            answer.append("1")
        else :
            answer.append("0")
    return ' '.join(answer)
    


if __name__ == "__main__":
    print(soluction())
    