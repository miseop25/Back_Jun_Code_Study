import sys
#input=sys.stdin.readline

N, M = map(int, input().split(" "))

poketMonList = []
poDict = dict()

for i in range(N) :
    buf = input()
    poketMonList.append(buf)
    poDict[buf] = i+1

# print("dict", poDict)
# print("list", poketMonList)

for _ in range(M):
    buf = input()
    if buf.isdigit() :
        ans = int(buf) - 1 
        print(poketMonList[ans])
    else :
        ans = poDict[buf]
        print(str(ans))
