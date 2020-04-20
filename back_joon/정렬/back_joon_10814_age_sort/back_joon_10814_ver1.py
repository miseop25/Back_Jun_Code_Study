import sys

N = int(sys.stdin.readline())
people = dict()

for i in range(N) : 
    age , name = sys.stdin.readline().split(' ' )
    name = name[0:-1]
    people[name] = [int(age), i]

people = sorted(people.items(), key=lambda t: (t[1][0], t[1][1]) )
for i in range(len(people)) :
        print(people[i][1][0], people[i][0])



