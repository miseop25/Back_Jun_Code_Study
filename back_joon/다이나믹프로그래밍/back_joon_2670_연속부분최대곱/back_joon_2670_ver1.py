import sys
input = sys.stdin.readline

def soluction(N) :
    if N == 1 :
        return float(input())
    result = []
    array = [float(input())]
    array.append(float(input()))

    comp = array[1]*array[0]

    for i in range(2, N) :
        num = float(input())
        if comp*num > num*array[i-1] :
            if comp > comp*num :
                result.append(comp)
            comp = comp*num
        else :
            result.append(comp)
            comp = num*array[i-1]
        array.append(num)
    result.append(comp)
    answer = max(result)

    return answer




if __name__ == "__main__":
    N = int(input())
    ans = soluction(N)
    ans = round(ans, 3)
    print(ans)