import sys
input = sys.stdin.readline

num = []
while True :
    num = list(map(int, input().split(" ")))
    if 0 in num :
        break
    num = sorted(num, key= lambda x: -x)
    print(num)
    if num[0]**2 == (num[1]**2 + num[2]**2) :
        print("right")
    else :
        print("wrong")

