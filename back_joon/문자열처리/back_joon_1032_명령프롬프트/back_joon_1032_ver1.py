import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    answer = list(input().rstrip())
    for _ in range(N-1) :
        temp = input().rstrip()
        for i in range(len(temp)) :
            if temp[i] == answer[i] :
                continue
            else :
                answer[i] = "?"
    print(''.join(answer))
