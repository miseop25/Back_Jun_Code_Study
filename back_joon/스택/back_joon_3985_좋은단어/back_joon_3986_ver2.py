import sys
input = sys.stdin.readline

def checkWord(word) :
    stackA = []
    stackB = []
    result = True
    i = 0 
    while i < len(word) :
        if i + 1 < len(word) :
            if word[i] == word[i+1] :
                i += 2
                continue

        if word[i] == "A" :
            if stackA :
                if stackB :
                    if stackB[0] > stackA[0] :
                        return False
                stackA.pop()
            else :
                stackA.append(i)
        elif word[i] == "B" :
            if stackB :
                if stackA :
                    if stackA[0] > stackB[0] :
                        return False
                stackB.pop()
            else :
                stackB.append(i)
        i += 1
    if stackB or stackA :
        return False
    return result


if __name__ == "__main__":
    N = int(input())
    answer = 0
    for _ in range(N) :
        word = input().rstrip()
        if checkWord(word) :
            answer += 1
    print(answer)