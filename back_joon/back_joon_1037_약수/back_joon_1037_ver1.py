import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split(" ")))
anaser = max(num) * min(num)
print(anaser)