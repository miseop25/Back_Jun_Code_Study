import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))

poDict = dict()

for i in range(N) :
    buf = input().strip()
    poDict[buf] = i+1
    poDict[str(i+1)] = buf
print(poDict)
for _ in range(M):
    buf = input().strip()

    print(poDict[buf])
