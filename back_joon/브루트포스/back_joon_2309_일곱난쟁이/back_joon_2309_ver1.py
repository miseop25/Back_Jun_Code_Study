import sys
import itertools
input = sys.stdin.readline

if __name__ == "__main__":
    smallPeople = []
    for i in range(9) :
        smallPeople.append(int(input()))
    result = list(itertools.combinations(smallPeople, 7))
    for i in result :
        if sum(i) == 100 :
            answer = sorted(i)
            for j in answer :
                print(j)
            break
