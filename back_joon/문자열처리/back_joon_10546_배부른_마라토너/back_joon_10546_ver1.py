import sys
input = sys.stdin.readline

N = int(input())
# person : 참가한 사람들의 dict
# finish : 완주한 사람들의 dict
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
    #  참가자에는 있지만 완주자에는 없다면 해당 키가 정답
    if n not in finish :
        answer = n
        break
    else :
        #  참가자의 value와 완주자의 value가 다르다면 해당 키가 정답
        if person[n] != finish[n] :
            answer = n
            break
print(answer)