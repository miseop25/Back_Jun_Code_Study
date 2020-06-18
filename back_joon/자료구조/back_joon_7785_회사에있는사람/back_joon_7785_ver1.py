import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    enterDict = dict()
    for _ in range(N) :
        name, status = map(str, input().rstrip().split(" "))
        if status == "enter" :
            enterDict[name] = 0
        else :
            del enterDict[name]
    answer = sorted(enterDict.keys(), reverse= True)
    for i in answer :
        print(i)