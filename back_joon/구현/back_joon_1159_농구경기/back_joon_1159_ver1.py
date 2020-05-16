import sys
input = sys.stdin.readline

N = int(input())

name = dict()
for _ in range(N) :
    temp = input().rstrip()
    if temp[0] in name :
        name[temp[0]] += 1
    else :
        name[temp[0]] = 1


result = []
for i in name.items() :
    if i[1] >= 5 :
        result.append(i[0])
if result :
    result = sorted(result)
    print("".join(result))
else :
    print("PREDAJA")