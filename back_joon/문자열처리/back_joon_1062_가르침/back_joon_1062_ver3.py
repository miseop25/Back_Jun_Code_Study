import sys
import collections
import itertools
input = sys.stdin.readline


def soluction() :
    N, K = map(int, input().split(" "))
    already = ['a', 'c', 't', 'i','n']
    index_list = [0 for _ in range(26)]
    for i in already :
        index_list[ord(i)-97] = 1
    K = K - 5

    words = []
    for _ in range(N) :
        buf = input().lstrip("anta").rstrip("tica\n")
        words.append(buf)
    #  모든 남극어는 a, c, t, i, n을 포함하기 때문에!!
    if K < 0 :
        return 0
    pos = []
    total = []
    for i in words :
        temp = index_list.copy()
        check = True
        cnt = 0
        buf = []
        for j in i :
            if temp[ord(j) - 97] == 0 :
                temp[ord(j) - 97] = 1
                buf.append(j)
                cnt += 1
            if cnt > K :
                check = False
                break
        if check :
            pos.append(temp)
            for d in buf :
                if index_list[ord(d) - 97] == 0 :
                    index_list[ord(d) - 97] = 1
                    total.append(d)

    charaters = list(itertools.combinations(total, 10))
    print(charaters)
    ans_list = []
    for ch in charaters :
        cnt = 0
        for p in pos :
            check = True
            for r in ch :
                if p[ord(r) - 97] != 1 :
                    check = False
            if check :
                cnt += 1
        ans_list.append(cnt)
    return max(ans_list)


print(soluction())
