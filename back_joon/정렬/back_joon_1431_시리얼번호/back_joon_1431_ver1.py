import sys
input = sys.stdin.readline


def sun_num(s) :
    answer = 0
    for i in s :
        if i >= '0' and i <= '9' :
            answer += int(i)
    return answer

N = int(input())
serial_num = []
for _ in range(N):
    serial_num.append(input().strip())

serial_num = sorted(serial_num , key= lambda x : (len(x), sun_num(x), x))

for i in serial_num :
    print(i)