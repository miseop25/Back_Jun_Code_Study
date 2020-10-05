import sys
input = sys.stdin.readline


def soluction(word) :
    alpaDict = dict()
    for i, v in enumerate(word) :
        if v in alpaDict :
            if alpaDict[v] == i -1 :
                alpaDict[v] = i
            else :
                return False
        else :
            alpaDict[v] = i
    return True


if __name__ == "__main__":
    N = int(input())
    answer = 0
    for _ in range(N) :
        if soluction(input().rstrip()) :
            answer += 1
    print(answer)

        
