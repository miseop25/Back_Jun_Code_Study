import sys
import math
import collections
input = sys.stdin.readline

N, H = map(int, input().split(" "))
even = []
odd = []
answer = [N//2, 2]
for i in range(N) :
    temp = int(input())
    if i%2 == 0 :
        even.append(temp)
    else :
        odd.append(H - temp)
even = collections.deque(sorted(even))
odd = collections.deque(sorted(odd))
buf1 = 0
buf2 = 0




ans = str(answer[0]) + " " + str(answer[1])
print(ans)

