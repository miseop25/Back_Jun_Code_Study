import sys
from collections import deque
input = sys.stdin.readline

def soluction() :
    cmd = input().rstrip()
    n = int(input())
    if n != 0 :
        num = deque(list(map(int, input().lstrip("[").rstrip("]\n").split(","))))
    else :
        _ = input()
        num = deque([])
    
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
        return list(num)
    else :
        num.reverse()
        return list(num)



if __name__ == "__main__":
    T = int(input())
    for _ in  range(T) :
        print(soluction())