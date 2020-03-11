import sys
import math
input = sys.stdin.readline

N = int(input())
answer = 0 




def makeRootList(first_root) :
    root_list = []
    for i in range(1, first_root +1) :
        root_list.append(i)
    return root_list

def getMinCount(root_lsit, num, cnt) :
    answr_lsit = []
    ans = 0
    for i in root_list :
        ans = num - math.pow(i, 2)
        if ans == 0 :
            answr_lsit.append(cnt+1)
            answr_lsit = sorted(answr_lsit)
        elif ans >0 :
            cnt += 1
            first_root = math.sqrt(ans)
            first_root = math.floor(first_root)
            new_root_list = makeRootList(first_root)
            cnt = getMinCount(new_root_list, ans, cnt)
            answr_lsit.append(cnt)

    return min(answr_lsit)







first_root = math.sqrt(N)
first_root = math.floor(first_root)
root_list = makeRootList(first_root)

a = getMinCount(root_list, N, 0)

print(a)

