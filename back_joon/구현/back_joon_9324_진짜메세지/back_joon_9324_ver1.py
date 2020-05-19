import sys
input = sys.stdin.readline

def soluction(message) :
    answer = "OK"
    alpa = dict()
    for i in range(26) :
        alpa[chr(65 + i)] = 0
    i = 0
    while i < len(message) :
        alpa[message[i]] += 1
        if alpa[message[i]] == 3 :
            if i + 1 < len(message) :
                if message[i+1] != message[i] :
                    return "FAKE"
            else : 
                return "FAKE"
            alpa[message[i]] = 0
            i += 2
        else :
            i += 1
    return answer

if __name__ == "__main__":
    N = int(input())
    for _ in range(N) :
        print(soluction(input().rstrip()))
