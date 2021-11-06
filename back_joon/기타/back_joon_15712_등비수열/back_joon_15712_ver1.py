import sys
input = sys.stdin.readline

a, r, n, mods = map(int, input().rstrip().split(" "))

t = a
tr = 1
testSet = set()
testArr = []
for i in range(mods) :
    m = t%mods
    if m not in testSet :
        testSet.add(m)
        testArr.append(m)
    elif m in testSet :
        break
    tr *= r
    t += tr

sLen = len(testSet)

if n != 1 :
    targetIndex = int((n) % sLen)
    print(testArr[targetIndex - 1])
else :
    print(a)