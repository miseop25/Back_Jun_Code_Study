import sys
input = sys.stdin.readline

def mult(arrays) :
    if not arrays :
        return 0
    result = arrays[0]
    for i in arrays[1:] :
        result *= i
    return result

def soluction() :
    answer = 0
    case = int(input())
    if case == 0 :
        return 0
    cloths = dict()
    for _ in range(case) :
        _, keys = map(str, input().rstrip().split(" ") )
        if keys in cloths :
            cloths[keys] += 1 
        else :
            cloths[keys] = 2
    result = list(sorted(cloths.values()))
    answer = mult(result) - 1
    return answer


if __name__ == "__main__":
    N = int(input())
    for _ in range(N) :
        print(soluction())
