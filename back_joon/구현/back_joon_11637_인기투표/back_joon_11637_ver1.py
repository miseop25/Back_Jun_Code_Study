import sys
input = sys.stdin.readline

def soluction() :
    n = int(input())
    person = dict()
    total = 0
    for i in range(1, n+1) :
        temp = int(input())
        person[i] = temp
        total += temp

    result = sorted(person.items(), key = lambda x: -x[1])

    if result[0][1] == result[1][1] :
        return "no winner"
    elif result[0][1] > total//2 :
        return "majority winner " + str(result[0][0])
    else :
        return "minority winner " + str(result[0][0])
    


if __name__ == "__main__":
    T = int(input())
    for _ in range(T) :
        print(soluction())
