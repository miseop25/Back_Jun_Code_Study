import sys
from operator import itemgetter, attrgetter
input = sys.stdin.readline

N, K = map(int, input().split(" "))
oplimpic_result = []
for _ in range(N) :
    buf = list(map(int, input().split(" ")))
    oplimpic_result.append(buf)

oplimpic_result = sorted(oplimpic_result, key= itemgetter(1,2,3) , reverse= True)
answer = 1
same = 0
for i in range(N) :
    if i != 0 :
        if oplimpic_result[i][1] == oplimpic_result[i-1][1] and oplimpic_result[i][2] == oplimpic_result[i-1][2] and oplimpic_result[i][3] == oplimpic_result[i-1][3] :
            answer = answer
            same += 1
        else :
            answer = answer + 1 + same
            same = 0

    if oplimpic_result[i][0] == K :
        print(answer)
        break
        

