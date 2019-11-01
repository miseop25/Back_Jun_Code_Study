import operator
import sys

N = int(sys.stdin.readline())
people = dict()

for i in range(N) : 
    age , name = sys.stdin.readline().split(' ' )
    name = name.split()
    people[name[0]] = int(age)

people = sorted(people.items(), key=operator.itemgetter(1))
#people = sorted(people.items(), key=lambda t: t[1])
for i in range(N) :
    print(people[i][1], people[i][0])

