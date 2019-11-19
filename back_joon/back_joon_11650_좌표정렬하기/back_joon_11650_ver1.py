import sys
from operator import itemgetter , attrgetter
input=sys.stdin.readline

N = int(input())
num_listt = []
for _ in range(N) :
    num_listt.append(tuple(map(int , input().split(' '))))

num_listt = sorted(num_listt, key=itemgetter(0,1))
for i in num_listt :
    print(i[0], i[1])


