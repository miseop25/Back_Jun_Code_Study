import sys
input = sys.stdin.readline


def soluction() :
    word = input().rstrip()
    num = []
    temp = 0
    isnum = False
    for i in range(len(word)) :
        if word[i] >= "0" and word[i] <= "9" :
            if not isnum :
                temp = i
            isnum = True
        else :
            if isnum :
                num.append(int(word[temp: i]))
            isnum = False
    if isnum :
        num.append(int(word[temp :]))
    return num


if __name__ == "__main__":
    N = int(input())
    answer = []
    for _ in range(N) :
        answer.extend(soluction())
    answer = sorted(answer)       
    for i in answer :
        print(i) 
    