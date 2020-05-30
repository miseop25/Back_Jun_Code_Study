import sys
input = sys.stdin.readline

if __name__ == "__main__":
    findStr = input().rstrip()
    f_len = len(findStr)
    N = int(input())
    answer = 0
    for _ in range(N):
        string = input().rstrip()
        string += string[ : len(findStr)-1]
        
        for i in range(len(string) - f_len + 1) :
            # print(string[i : f_len + i])
            if string[i : f_len + i] == findStr :
                answer += 1
                break

    print(answer)

