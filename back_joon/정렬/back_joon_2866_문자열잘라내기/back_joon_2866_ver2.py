import sys
import math
input = sys.stdin.readline


def checkWord(start, end) :
    chword = dict()
    for string in word :
        buf = string[start : end]
        if buf in chword :
            return False
        else :
            chword[buf] = True
    return True

def binarySerch(left, right, answer) :
    mid = math.floor((right + left)//2)
    flag = checkWord(mid, right)
    if flag :
        left = mid
        if answer < mid :
            answer = mid
    else :
        right = mid
        if answer > mid :
            answer = mid

    return left, right, answer, flag


if __name__ == "__main__":
    answer = 0
    R, C = map(int, input().split(" "))
    first_word = input().rstrip()
    word_list = list([] for i in range(C))
    for _ in range(R-1) :
        tmep = input().rstrip()
        for j in range(C) :
            word_list[j].append(tmep[j])
    
    word = []
    for i in word_list :
        word.append("".join(i))

    left = 0
    right = R-1

    while True :
        left, right, answer, flag = binarySerch(left, right, answer)
        m =(right + left)//2

        if m == left or m == right :
            break

    if answer != 0 :
        print(answer + 1)
    else :
        if flag :
            print(answer+1)
        else :
            print(answer)

