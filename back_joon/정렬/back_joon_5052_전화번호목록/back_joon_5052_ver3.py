import sys
import collections

input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    N = int(input())
    answer = True
    hd = dict()
    for i in range(N):
        buf = input().rstrip()
        if buf[0] in hd :
            hd[buf[0]].append(buf)
        else :
            hd[buf[0]] = [buf]

    for i in hd.values() :
        i = collections.deque(sorted(i))
        while i and answer :
            check = i.popleft()
            if i :
                if len(check) <= len(i[0]) :
                    if check == i[0][:len(check)] :
                        answer = False



    if answer :
        print("YES")
    else :
        print("NO")
