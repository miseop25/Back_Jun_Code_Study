import sys
input = sys.stdin.readline

if __name__ == "__main__":
    answer = 0
    for x in range(8) :
        temp = input().rstrip()
        for y in range(4) :
            if x%2 == 0 :
                if temp[2*y] == "F" :
                    answer += 1
            else :
                if temp[y * 2 - 1] == "F" :
                    answer += 1

    print(answer)
