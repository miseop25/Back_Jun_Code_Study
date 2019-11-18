import sys
input=sys.stdin.readline


N, M  = map(int, input().split(' '))

num_list = []
for _ in range(N) :
    num_list.append(list(map(int, input().split(' '))))    
k = int(input())

for _ in range(k) :
    i,j,x,y = map(int, input().split(' '))
    answer = 0
    for a in range(i,x+1) :
        for b in range(j,y+1) :
            answer += num_list[a-1][b-1]

    print(answer)