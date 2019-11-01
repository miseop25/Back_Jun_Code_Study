import sys

N = int(sys.stdin.readline())
people = list()

for i in range(N) : 
    age , name = sys.stdin.readline().split(' ' )
    name = name[0:-1]
    people.append([int(age), name , i])

people.sort(key=lambda x: (x[0], x[2]))
for i in range(len(people)) :
        print(people[i][0], people[i][1])



