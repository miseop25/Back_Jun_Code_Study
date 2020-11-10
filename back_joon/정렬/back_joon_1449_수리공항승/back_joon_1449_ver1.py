import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, L = map(int, input().split(" "))
    location = list(map(int, input().split(" ")))
    location = sorted(location)
    answer = 0
    check = 0 
    for i in location :
        if check < i :
            answer += 1
            check = i + L - 1
    print(answer)
