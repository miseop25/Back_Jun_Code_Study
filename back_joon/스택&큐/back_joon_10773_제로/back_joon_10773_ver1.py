import sys
input = sys.stdin.readline

if __name__ == "__main__":
    K = int(input())
    answer = 0
    stack = []
    for _ in range(K) :
        val = int(input())
        if val == 0 :
            if stack :
                answer -= stack.pop()
        else :
            answer += val
            stack.append(val)
    print(answer)
