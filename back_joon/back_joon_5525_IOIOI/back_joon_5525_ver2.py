import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
string = input().rstrip()
answer = 0
i = -1
while i < M-3 :
    i += 1
    if string[i] == "I" :
        o_cnt = 0
        while string[i+1] == "O" and string[i+2] == "I" :
            o_cnt += 1
            i += 2
            if o_cnt == N :
                o_cnt -= 1
                answer += 1
            if i > M-2 :
                break

print(answer)


