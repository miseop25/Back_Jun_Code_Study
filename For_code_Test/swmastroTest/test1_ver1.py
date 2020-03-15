import sys
input = sys.stdin.readline

N = int(input())
num = [6,2,5,5,4,5,6,3,8,7]
ok_num = []
answer = []
for i in range(10) :
    if N >= num[i] :
        ok_num.append(i)

for i in ok_num :
    buf = N
    ans = ''
    while buf >=0 :
        buf = buf - num[i]
        if buf >= 0:
            ans += str(i)
            answer.append(int(ans))

print(max(answer))

