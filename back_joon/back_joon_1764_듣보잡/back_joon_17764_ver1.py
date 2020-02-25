import sys
input=sys.stdin.readline

N, M = map(int, input().split(" "))

dosentSee = set()
dosentHear = set()

for _ in range(N) :
    dosentSee.add(str(input()))

for _ in range(M) :
    dosentHear.add(str(input()))

answer = list(dosentHear.intersection(dosentSee))
answer.sort()

print(len(answer))
for i in answer :
    sys.stdout.write(i)

