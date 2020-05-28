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

def binarySerch(left, right, end) :
    global answer
    if left > right :
        return
    mid = math.floor((right + left)/2)
    flag = checkWord(mid, end)
    if flag :
        if answer < mid :
            answer = mid
        binarySerch(mid + 1, right, end)
    else :
        binarySerch(left, mid - 1, end)

answer = 0
R, C = map(int, input().split(" "))
word_list = list([] for i in range(C))
for _ in range(R) :
    tmep = input().rstrip()
    for j in range(C) :
        word_list[j].append(tmep[j])
    
word = []
for i in word_list :
    word.append("".join(i))

binarySerch(0, R, R)

print(answer)

