import sys
import math
input = sys.stdin.readline

N = int(input())

num_str = str(math.factorial(N))

num_str = num_str[::-1]

for i in num_str :
    if i != "0" :
        print(i)
        break

