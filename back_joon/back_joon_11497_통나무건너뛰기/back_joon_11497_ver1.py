import sys
import collections

input = sys.stdin.readline

T = int(input())

for _ in range(T) : 
    num = int(input())
    tree_list = list(map(int, input().split(" ")))
    tree_list = sorted(tree_list)
    deq = collections.deque([])

    for i in range(len(tree_list)-1, -1 , -1) :
        if i%2 == 1 :
            deq.appendleft(tree_list[i])
        else :
            deq.append(tree_list[i])

    ans = abs(deq[-1] - deq[0])
    for j in range(1, len(deq)) :
        buf = abs(deq[j]- deq[j-1])
        if buf > ans :
            ans = buf
    
    print(ans)
