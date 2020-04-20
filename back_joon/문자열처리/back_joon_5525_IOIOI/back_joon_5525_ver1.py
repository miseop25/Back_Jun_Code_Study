import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
string = input().rstrip()
pn = "I" + ("OI" * N)
answer = 0
i = 0
while i < M :
    if string[i] == "I" :
        try :
            if string[i : i+len(pn)] == pn :
                answer += 1
                i = i + 2
            else :
                i += 1
        except :
            break
    else :
        i += 1
print(answer)


