import sys
import math
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
even.sort()
odd.sort()

for i in range(1, math.ceil(H/2)) :
    check = 0
    for j in range(N//2) :
        if even[j] > i :
            check += 1
        if odd[j] <= i :
            check += 1
    if check < answer[0] :
        answer[0] = check
        answer[1] = 1
    elif check == answer[0] :
        answer[1] += 1

ans = str(answer[0]) + " " + str(answer[1])
print(ans)
print(even)
print(odd)
        
