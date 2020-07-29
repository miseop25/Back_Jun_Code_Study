import sys
input = sys.stdin.readline

def makeNewAvg(a, b) :
    return a/b*100

if __name__ == "__main__":
    n = int(input())
    score = list(map(int, input().split(" ")))
    score = sorted(score)
    total = 0
    for i in score :
        total += makeNewAvg(i, score[-1])
    print(total/n)
