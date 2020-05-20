import sys
import itertools
input = sys.stdin.readline

def soluction() :
    answer = 0
    case = int(input())
    cloths = dict()
    for _ in range(case) :
        value, keys = map(str, input().rstrip().split(" ") )
        if keys in cloths :
            cloths[keys].append(value)
        else :
            cloths[keys] = [value]
    
    result = sorted(cloths.values())
    temp = list(itertools.product(*result))
    print(temp)

    temp = list(itertools.product(result[0] ) )
    print(temp)
    return answer



if __name__ == "__main__":
    N = int(input())
    for _ in range(N) :
        print(soluction())
