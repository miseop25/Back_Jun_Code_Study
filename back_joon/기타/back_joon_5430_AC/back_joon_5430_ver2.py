import sys
from collections import deque
t = open("/Users/minseopkim/Documents/GitHub/Back_Jun_Code_Study/back_joon/기타/back_joon_5430_AC/I.in", 'r')
r = open("/Users/minseopkim/Documents/GitHub/Back_Jun_Code_Study/back_joon/기타/back_joon_5430_AC/I.out", "r")

input = t.readline

def soluction() :
    cmd = input().rstrip()
    n = int(input())
    if n != 0 :
        num = deque(list(map(str, input().lstrip("[").rstrip("]\n").split(","))))
    else :
        _ = input()
        if "D" in cmd :
            return "error"
        else :
            return '[]'
    
    flag = True
    for i in cmd :
        if i == "D" :
            if num :
                if flag :
                    num.popleft()
                else :
                    num.pop()
            else :
                return "error"
        elif i == "R" :
            if flag :
                flag = False
            else :
                flag = True
            # flag = False if flag else True
    if flag :
        pass
    else :
        num.reverse()
    answer = "[" + ','.join(num) + "]"
    return answer


if __name__ == "__main__":
    
    T = int(input())
    for a in  range(T) :
        comp = r.readline().rstrip()
        answer = soluction()
        if comp != answer :
            print(a)
            break

    r.close()
    t.close()