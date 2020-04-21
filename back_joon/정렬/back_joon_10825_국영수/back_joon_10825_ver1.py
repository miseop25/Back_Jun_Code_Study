import sys
input = sys.stdin.readline

N = int(input())
student = []
for _ in range(N) :
    buf = list(map(str, input().rstrip().split(" ")))
    student.append(buf)
student = sorted(student, key= lambda x: ( -int(x[1]), int(x[2]), -int(x[3]), x[0] ) ) 

for i in student :
    print(i[0])