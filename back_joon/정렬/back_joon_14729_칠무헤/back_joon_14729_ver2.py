import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    num = []
    for i in range(T) :
        temp = input().rstrip()
        num.append(float(temp))
        if i > 8 :
            num = sorted(num)
            num.pop()
    num = sorted(num)
    for i in range(7) :
        print('%0.3f' % float(num[i]))
