import sys
import collections

input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    N = int(input())
    num = collections.deque([])
    answer = True

    for i in range(N):
        num.append(input().rstrip())
    num = collections.deque(sorted(num))

    while num and answer :
        check = num.popleft()
        if num :
            if check in num[0] :
                answer = False
                break

    if answer :
        print("YES")
    else :
        print("NO")
