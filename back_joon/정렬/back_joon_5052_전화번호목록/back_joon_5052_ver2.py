import sys
import collections
import time

input = sys.stdin.readline
start_time = time.time()

t = int(input())
for _ in range(t) :
    N = int(input())
    num = collections.deque([])
    answer = True

    for i in range(N):
        num.append(input().rstrip())
    num = collections.deque(sorted(num, key= lambda x :len(x)))
    while num and answer :
        check = num.popleft()
        for j in num :
            if check == j[:len(check)] :
                answer = False
                break
    if answer :
        print("YES")
    else :
        print("NO")


end_time = time.time() - start_time
print(end_time)