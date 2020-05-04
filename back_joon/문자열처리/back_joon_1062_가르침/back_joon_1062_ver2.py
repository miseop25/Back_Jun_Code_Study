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
    answer = 0
    for _ in range(N) :
        buf = input().lstrip("anta").rstrip("tica\n")
        words.append(buf)
    #  모든 남극어는 a, c, t, i, n을 포함하기 때문에!!
    if K < 0 :
        return 0

    pos = []
    t = dict()
    for i in words :
        buf = []
        for j in i :
            if index_list[ord(j)-97] == 0 :
                buf.append(j)
        buf = list(set(buf))
        if len(buf) <= K :
            pos.append(buf)
            for a in buf :
                if a not in t :
                    t[a] = 1
                else :
                    t[a] += 1
    print(pos)
    t = sorted(t.items(), key= lambda x: (x[0]))
    print(t)

soluction()
