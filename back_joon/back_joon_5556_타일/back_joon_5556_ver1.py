import sys
input = sys.stdin.readline

N = int(input())
for _ in range(int(input())) :
    a, b = map(int,input().split(" "))
    a -= 1
    b -= 1
    cnt = 0

    for i in range(N) :
        if (a == i and b <= (N-i) and b >= i) or (b == i and a <= (N-i) and a >= i) or (b >=i and b <=(N-i) and a ==(N-1)) or (b == (N-1) and a >= i and a <=(N-i)) :
            break
        else :
            cnt += 1
    print(1 + cnt%3)