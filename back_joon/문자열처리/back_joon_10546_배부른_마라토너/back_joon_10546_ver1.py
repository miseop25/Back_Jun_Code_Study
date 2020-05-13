import sys
input = sys.stdin.readline

N = int(input())
person = dict()
finish = dict()
answer = ""
for _ in range(N) :
    name = input().rstrip()
    if name in person :
        person[name] += 1
    else :
        person[name] = 1

for _ in range(N-1) :
    name = input().rstrip()
    if name in finish :
        finish[name] += 1
    else :
        finish[name] = 1

for n in person.keys() :
    if n not in finish :
        answer = n
        break
    else :
        if person[n] != finish[n] :
            answer = n
            break
print(answer)