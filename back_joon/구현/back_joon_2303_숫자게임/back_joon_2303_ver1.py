import sys
from itertools import combinations
input = sys.stdin.readline


def maxSum(array) :
    temp = combinations(array, 3)
    result = 0
    for i in temp :
        buf = sum(i)
        comp = str(buf)
        if int(comp[-1]) > result :
            result = int(comp[-1])
    return result


if __name__ == "__main__":
    N = int(input())
    person = dict()
    for i in range(1, N+1) :
        temp = list(map(int, input().split(" ")))
        person[i] = maxSum(temp)
    result = sorted(person.items(), key = lambda x: (-x[1], -x[0]))
    print(result[0][0])


