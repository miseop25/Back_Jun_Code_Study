import sys
input = sys.stdin.readline
minSick = {"a": "A", "b": "B", "k":"C",
            "d": "D", "e":"E", "g":"F", 
            "h":"G", "i":"H", "l":"I",
            "m":"J", "n":"K",
            "o":"M", "p":"N", "r":"O",
            "s":"P", "t":"Q", "u":"R",
            "w":"S","y":"T"
            }

def changeMinSick(word) :
    result = word.replace("ng", "L")
    for k, v in minSick.items() :
        result = result.replace(k, v)
    return result
        
def soluction(array) :
    result = dict()
    for i in array: 
        tmep = changeMinSick(i)
        result[i] = tmep
    result = sorted(result.items(), key= lambda x : x[1])
    return result


if __name__ == "__main__":
    array = []
    N = int(input())
    for _ in range(N) :
        array.append(input().rstrip())
    answer = soluction(array)
    for i in answer :
        print(i[0])
