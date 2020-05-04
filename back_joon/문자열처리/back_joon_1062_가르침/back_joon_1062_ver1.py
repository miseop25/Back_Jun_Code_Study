import sys
import itertools
input = sys.stdin.readline

N, K = map(int, input().split(" "))
already = ['a', 'c', 't', 'i','n']
K = K - 5
words = []
answer = 0
for _ in range(N) :
    buf = input().lstrip("anta").rstrip("tica\n")
    words.append(buf)
# print(words)

know = []
pos = []
for i in words :
    if i == "" :
        answer += 1
    else :
        cnt = 0
        temp = []
        for s in i :
            if s not in already :
                cnt += 1
                temp.append(s)
        if cnt <= K :
            pos.append(temp)
            for j in temp :
                if j not in know :
                    know.append(j)
possibility = itertools.combinations(know, K)
ans_list = []
# print("know : ", know)
# print(pos)
for i in possibility :
    cnt = 0
    for j in pos :
        check = True
        for a in j :
            if a not in i :
                check = False
        if check :
            cnt += 1
    ans_list.append(cnt)

print(max(ans_list)+ answer)



