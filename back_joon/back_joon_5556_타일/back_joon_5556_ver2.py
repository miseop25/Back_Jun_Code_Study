import sys
import math
input = sys.stdin.readline

N = int(input())
color = [1,2,3]
for _ in range(int(input())) :
    a, b = map(int,input().split(" "))
    a -= 1
    b -= 1
    one_point = N/2
    x = a - one_point
    y = b - one_point
    degree = math.degrees( math.atan2(y,x) )
    if degree > -45 and degree < 45 :
        a = N -a -1
        print(color[a%3])
    elif degree > 45 and degree < 135:
        b = N - b -1
        print(color[b%3])
    elif degree > 135 :
        print(color[a%3])
    elif degree < -135 :
        print(color[a%3])
    elif degree > -135 and degree < -45 :
        print(color[b%3])
    else :
        print(color[a%3])
        
